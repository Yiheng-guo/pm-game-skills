# tower-defense: acceptance scenarios

1. A complete wave spends currency, follows lanes and resolves victory or base damage. Record the fixture, action, expected result and observed result.
2. Blocked lanes, sold towers and final-enemy death cannot stall wave completion. Record the fixture, action, expected result and observed result.
3. Projectiles and target listeners are cleaned when their tower or target disappears. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
