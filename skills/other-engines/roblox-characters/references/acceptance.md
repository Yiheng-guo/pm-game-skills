# roblox-characters: acceptance scenarios

1. A character can spawn, act, die and respawn with working controls. Record the fixture, action, expected result and observed result.
2. CharacterAdded races, missing Humanoid and R6/R15 differences recover. Record the fixture, action, expected result and observed result.
3. Character-scope connections are disposed on CharacterRemoving. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
