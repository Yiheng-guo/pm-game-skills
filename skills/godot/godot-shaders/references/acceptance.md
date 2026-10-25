# godot-shaders: acceptance scenarios

1. The shader compiles and renders on the selected Godot renderer. Record the fixture, action, expected result and observed result.
2. Unsupported feature, transparent edge and extreme uniform values have a fallback. Record the fixture, action, expected result and observed result.
3. Shared ShaderMaterial changes are isolated when per-object effects are intended. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
