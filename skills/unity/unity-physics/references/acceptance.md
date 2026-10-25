# unity-physics: acceptance scenarios

1. The intended collision or trigger event occurs exactly once per event. Record the fixture, action, expected result and observed result.
2. Kinematic/static pairs, tunneling and spawn overlaps are covered. Record the fixture, action, expected result and observed result.
3. Input is sampled separately from FixedUpdate force application. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
