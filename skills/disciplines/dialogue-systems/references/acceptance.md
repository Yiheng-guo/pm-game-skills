# dialogue-systems: acceptance scenarios

1. Every offered choice reaches a valid node and updates the intended flags. Record the fixture, action, expected result and observed result.
2. A missing target, cyclic auto-advance or invalid condition is detected without hanging. Record the fixture, action, expected result and observed result.
3. Save and restore preserve choice consequences without repeating rewards. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
