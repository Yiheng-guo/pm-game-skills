# physics-tuning: acceptance scenarios

1. Movement and contact outcomes are comparable at low and high render rates. Record the fixture, action, expected result and observed result.
2. Thin walls, fast bodies and stacked objects do not tunnel or explode under the target settings. Record the fixture, action, expected result and observed result.
3. Pause and resume do not inject a huge accumulated timestep. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
