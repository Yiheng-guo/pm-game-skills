# puzzle: acceptance scenarios

1. A known solution reaches the goal under the real action and move-budget rules. Record the fixture, action, expected result and observed result.
2. Illegal moves, unsolvable starts, repeated input and last-move wins resolve unambiguously. Record the fixture, action, expected result and observed result.
3. Undo restores the complete board and move budget while assistance remains disclosed. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
