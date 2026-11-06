# GPU fault drill

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Card start limit 400 W; step 60 s; commit e3b05dc.

PASS  crash: the governor killed outright, the watchdog handed the card back (limit 400 W, start 400 W)
PASS  switch: the master switch pulled, the governor handed back and exited (limit 400 W)
PASS  switch: while OFF, a governor refuses to start
PASS  blind: the response-time feed stopped, the governor failed up (ceiling to the top, the lid to the start)
PASS  end: the card at its own start limit (400 W)

Passed 5 of 5.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
