# unreal-behavior-trees: acceptance scenarios

1. A possessed pawn runs the tree and responds to a blackboard change. Record the fixture, action, expected result and observed result.
2. Missing controller, unreachable target and branch abort recover. Record the fixture, action, expected result and observed result.
3. Latent tasks finish or abort once and release callbacks. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
