import {finalizePresentation} from '/root/.codex/skills/builtins/presentations/container_tools/artifact_tool_utils.mjs';
const b='/workspace/scratch/f938a546368b';
const k='/root/.codex/skills/builtins/presentations';
const r=await finalizePresentation({
 workspaceDir:b,candidatePath:b+'/ch1_cases_build/candidate.pptx',finalPath:b+'/outputs/W5_CH1_두사례_보강_v3.pptx',
 pythonExecutable:process.env.CODEX_PRIMARY_RUNTIME_PYTHON,
 integrityValidatorPath:k+'/container_tools/inspect_presentation_package_integrity.py',
 layoutValidatorPath:k+'/container_tools/inspect_presentation_layout_geometry.py',
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit'],
 explicitTotalSlideCount:2,requiredNativeTableOwnerSlides:[],requiredNativeChartOwnerSlides:[],
 fontPolicy:{basis:'user_request',families:['Pretendard']},verifyArtifactToolImport:true,
 receiptPath:b+'/ch1_cases_build/validation_v3.json'
});console.log(JSON.stringify(r));
