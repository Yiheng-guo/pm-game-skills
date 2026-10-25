# unity-animation: acceptance scenarios

1. The controller transitions through idle, movement and the requested action. Record the fixture, action, expected result and observed result.
2. Interrupted triggers, missing Avatar and repeated enable do not stick in a state. Record the fixture, action, expected result and observed result.
3. Root motion and physics have a single intended owner. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
