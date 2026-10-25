# godot-tilemap: acceptance scenarios

1. A small painted level has matching visual, collision and navigation tiles. Record the fixture, action, expected result and observed result.
2. Boundary cells, empty cells and atlas changes do not create invisible blockers. Record the fixture, action, expected result and observed result.
3. Logical layers and TileSet resources use the project's actual Godot APIs. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
