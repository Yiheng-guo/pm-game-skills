# create-game-assets: acceptance scenarios

1. Player, enemies and environment share the agreed scale, palette and silhouette language. Record the fixture, action, expected result and observed result.
2. Transparent edges and nearest/linear filtering are checked at actual game scale. Record the fixture, action, expected result and observed result.
3. The manifest records license, source, dimensions and importer settings. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
