import path from 'node:path';
import fs from 'node:fs/promises';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
const skill=process.env.PRESENTATION_SKILL_ROOT||'/root/.codex/skills/builtins/presentations';
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const root=process.cwd();
const base=process.env.W8_BUILD_DIR;
if(!base) throw new Error('Set W8_BUILD_DIR');
const dest=process.env.W8_BUNDLE_DIR||path.resolve(path.dirname(new URL(import.meta.url).pathname),'..');
const slides=JSON.parse(await fs.readFile(path.join(dest,'w8_content.json'),'utf8')).slides;
const tableOwners=slides.filter(s=>['table','comparison'].includes(s.kind)).map(s=>s.page);
const finalPath=path.join(dest,'outputs/W8_AI_CCTV_draft_v1.pptx');
const result=await finalizePresentation({
 workspaceDir:root,candidatePath:path.join(base,'candidate.pptx'),finalPath,
 pythonExecutable:process.env.CODEX_PRIMARY_RUNTIME_PYTHON,
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','12188952,6858000','--validate-bullet-geometry','--validate-heading-fit',...tableOwners.flatMap(s=>['--require-native-table-slide',String(s)])],
 requiredNativeTableOwnerSlides:tableOwners,requiredNativeChartOwnerSlides:[9],materializeLiteralChartWorkbooks:true,
 fontPolicy:{basis:'design',families:['Pretendard']},
 verifyArtifactToolImport:true,receiptPath:path.join(base,'finalization.json')
});
console.log(JSON.stringify(result));
