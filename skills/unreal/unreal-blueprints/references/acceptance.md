# unreal-blueprints: acceptance scenarios

1. A reusable Blueprint instance completes its intended interaction. Record the fixture, action, expected result and observed result.
2. Repeated BeginPlay-like setup, missing references and destroyed actors are safe. Record the fixture, action, expected result and observed result.
3. The Construction Script does not perform runtime-only state changes. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
