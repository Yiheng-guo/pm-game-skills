# godot-signals-groups: acceptance scenarios

1. An emitted event reaches exactly the intended receivers. Record the fixture, action, expected result and observed result.
2. A freed receiver, repeated connect and group membership change cause no duplicate effects. Record the fixture, action, expected result and observed result.
3. Scene teardown disconnects long-lived publishers from short-lived listeners. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
