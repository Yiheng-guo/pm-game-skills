# bevy-ecs: acceptance scenarios

1. The locked Bevy version compiles and a minimal scene demonstrates the system behavior. Record the fixture, action, expected result and observed result.
2. Missing query matches, despawned entities and repeated state entry are safe. Record the fixture, action, expected result and observed result.
3. Scheduling order is explicit where one system reads another system's writes. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
