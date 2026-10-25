# rpg: acceptance scenarios

1. Quest progress, inventory, combat and rewards close one complete playable quest. Record the fixture, action, expected result and observed result.
2. Full inventory, repeated interaction and reloading before reward cannot duplicate grants. Record the fixture, action, expected result and observed result.
3. Save/load preserves equipment-derived stats and quest state. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
