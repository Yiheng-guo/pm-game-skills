# performance-optimization: acceptance scenarios

1. The same worst-case scene is measured before and after with device and sample duration. Record the fixture, action, expected result and observed result.
2. Peak entity count and long-session memory behavior are sampled without debug overlays. Record the fixture, action, expected result and observed result.
3. Optimization preserves state outcomes for a deterministic input replay. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
