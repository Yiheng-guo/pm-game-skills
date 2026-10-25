# godot-ui-control: acceptance scenarios

1. Menu and HUD remain usable after window resize and keyboard-only navigation. Record the fixture, action, expected result and observed result.
2. Long localized strings and a missing focus neighbor do not strand the player. Record the fixture, action, expected result and observed result.
3. Containers own child layout and modal overlays restore focus. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
