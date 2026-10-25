# godot-resources: acceptance scenarios

1. Two consumers can share configuration without sharing unintended run state. Record the fixture, action, expected result and observed result.
2. Missing resource and older serialized fields load safely. Record the fixture, action, expected result and observed result.
3. Runtime mutation uses a deliberate duplicate policy for nested resources. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
