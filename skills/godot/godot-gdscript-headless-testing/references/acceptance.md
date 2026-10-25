# godot-gdscript-headless-testing: acceptance scenarios

1. A fresh import followed by the test command returns zero only on success. Record the fixture, action, expected result and observed result.
2. An intentional assertion failure returns nonzero and terminates without hanging. Record the fixture, action, expected result and observed result.
3. Tests have bounded completion and do not depend on an existing import cache. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
