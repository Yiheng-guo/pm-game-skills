# roguelike: acceptance scenarios

1. A seeded run supports movement, turn combat, loot and an explicit end condition. Record the fixture, action, expected result and observed result.
2. Blocked movement, no legal spawn and simultaneous death have deterministic handling. Record the fixture, action, expected result and observed result.
3. Permadeath and continuation rules do not duplicate loot or preserve forbidden state. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
