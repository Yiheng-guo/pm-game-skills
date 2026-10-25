# phaser-arcade-physics: acceptance scenarios

1. A runnable scene confirms velocity, collisions and body size alignment. Record the fixture, action, expected result and observed result.
2. Static-body refresh, world bounds and fast contacts do not silently miss. Record the fixture, action, expected result and observed result.
3. Scene restart removes colliders and timers created by the prior scene. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
