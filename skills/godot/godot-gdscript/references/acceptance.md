# godot-gdscript: acceptance scenarios

1. The script parses and the attached scene exercises its public behavior. Record the fixture, action, expected result and observed result.
2. Null exported references, freed instances and invalid resources are handled. Record the fixture, action, expected result and observed result.
3. Lifecycle ownership prevents duplicate setup on scene re-entry. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
