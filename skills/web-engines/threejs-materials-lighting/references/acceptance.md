# threejs-materials-lighting: acceptance scenarios

1. The chosen PBR or unlit material is readable under the target lighting. Record the fixture, action, expected result and observed result.
2. Dark scenes, color-space mismatch and shadow acne are checked on target renderer. Record the fixture, action, expected result and observed result.
3. Cloned objects share or duplicate materials deliberately. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
