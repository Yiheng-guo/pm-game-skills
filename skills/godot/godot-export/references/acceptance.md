# godot-export: acceptance scenarios

1. A clean export opens at the correct entry scene outside the editor. Record the fixture, action, expected result and observed result.
2. Missing export templates, imported assets and relative paths are checked explicitly. Record the fixture, action, expected result and observed result.
3. Signing credentials and platform identifiers stay out of the repository. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
