# roblox-ui: acceptance scenarios

1. HUD and menus survive respawn and small-screen emulation. Record the fixture, action, expected result and observed result.
2. Touch, gamepad focus and overlapping layers cannot activate hidden controls. Record the fixture, action, expected result and observed result.
3. PlayerGui listeners are rebuilt once and old GUI state is released. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
