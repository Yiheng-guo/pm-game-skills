# unity-navmesh: acceptance scenarios

1. An agent reaches a valid target on the baked surface. Record the fixture, action, expected result and observed result.
2. Unreachable destinations, off-mesh starts and moving obstacles recover. Record the fixture, action, expected result and observed result.
3. Agent settings and baked geometry match the player dimensions. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
