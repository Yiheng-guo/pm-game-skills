# input-systems: acceptance scenarios

1. Each action fires once per intended press across supported bindings. Record the fixture, action, expected result and observed result.
2. Lost focus, held keys, touch cancellation and device switching do not leave stuck actions. Record the fixture, action, expected result and observed result.
3. Menus consume their actions so gameplay does not also receive them. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
