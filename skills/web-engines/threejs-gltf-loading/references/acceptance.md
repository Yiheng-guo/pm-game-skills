# threejs-gltf-loading: acceptance scenarios

1. A pinned GLTFLoader displays the model and plays the intended clip. Record the fixture, action, expected result and observed result.
2. Missing file, decoder and texture dependencies show an actionable fallback. Record the fixture, action, expected result and observed result.
3. Mixer actions stop and exclusively owned GPU resources are disposed. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
