import {finalizePresentation} from '/root/.codex/skills/builtins/presentations/container_tools/artifact_tool_utils.mjs';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import fs from 'node:fs';
const b=path.dirname(fileURLToPath(import.meta.url));
fs.mkdirSync(b+'/generated',{recursive:true});
const k='/root/.codex/skills/builtins/presentations';
const r=await finalizePresentation({
 workspaceDir:b,candidatePath:b+'/candidate.pptx',finalPath:b+'/generated/W5_CH1_통합보강_v1.pptx',
 pythonExecutable:process.env.CODEX_PRIMARY_RUNTIME_PYTHON,
 integrityValidatorPath:k+'/container_tools/inspect_presentation_package_integrity.py',
 layoutValidatorPath:k+'/container_tools/inspect_presentation_layout_geometry.py',
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit'],
 explicitTotalSlideCount:11,requiredNativeTableOwnerSlides:[],requiredNativeChartOwnerSlides:[],
 fontPolicy:{basis:'user_request',families:['Pretendard']},verifyArtifactToolImport:true,
 receiptPath:b+'/generated/validation.json'
});console.log(JSON.stringify(r));
