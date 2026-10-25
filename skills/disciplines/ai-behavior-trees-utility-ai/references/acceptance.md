# ai-behavior-trees-utility-ai: acceptance scenarios

1. A higher-priority threat interrupts a running action and its abort runs once. Record the fixture, action, expected result and observed result.
2. Equal utility scores have a deterministic tie-break; missing blackboard data fails safely. Record the fixture, action, expected result and observed result.
3. A despawned agent leaves no running task or listener. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
