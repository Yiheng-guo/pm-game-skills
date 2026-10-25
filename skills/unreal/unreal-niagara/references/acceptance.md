# unreal-niagara: acceptance scenarios

1. The effect renders at the intended world scale and ends on time. Record the fixture, action, expected result and observed result.
2. Burst repetition, culling and unavailable GPU features have defined behavior. Record the fixture, action, expected result and observed result.
3. Spawned systems are bounded and are destroyed or returned to a pool. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
