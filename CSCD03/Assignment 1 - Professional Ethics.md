# 1. Information Presentation Response

# 2. Ethical Advice 
Stakeholders: all 3 of them + the two customer businesses, competitor
**min 170 words each**
https://ethics.acm.org/code-of-ethics/software-engineering-code/
## Sandra
- As president, cares empirically about the status of the company
- Willing to fulfill the orders as both "problematic" customers are operating under legal means and company is heading towards bankruptcy
- Must consider tradeoffs
- Pros: company stays alive, fulfillment with main customer base
- Cons: possibly lowered reputation for some organizations, unhappy employees
- Should explicitly create a code of ethics for the company to ensure everyone is on the same page and have consequences if broken
- Everyone, all 20 employees should be gathered for the meeting
- Best to see if there are other employees that are able to perform the installations, if it is not possible, then heavily monitor the situation to ensure no sabotage happens
## Sam
- Bringing personal opinions to the business
- Greatly against abortion and willing to put matters into their own hands
- Very much violates working ethics
- Needs to realize that the customer is able to put the blame on the software for not working as intended and causing them serious issues
- If fired for the sabotage, it leaves a permanent imprint, causing issues in the future relating to other employment if companies do background checks
2.07. Identify, document, and report significant issues of social concern, of which they are aware, in software or related documents, to the employer or the client.
2.09. Promote no interest adverse to their employer or client, unless a higher ethical concern is being compromised; in that case, inform the employer or another appropriate authority of the ethical concern.
3.06. Work to follow professional standards, when available, that are most appropriate for the task at hand, departing from these only when ethically or technically justified.
3.12. Work to develop software and related documents that respect the privacy of those who will be affected by that software.
3.14. Maintain the integrity of data, being sensitive to outdated or flawed occurrences.
4.03. Maintain professional objectivity with respect to any software or related documents they are asked to evaluate.
4.05. Disclose to all concerned parties those conflicts of interest that cannot reasonably be avoided or escaped.

4.06. Refuse to participate, as members or advisors, in a private, governmental or professional body concerned with software related issues, in which they, their employers or their clients have undisclosed potential conflicts of interest.
6.01. Help develop an organizational environment favorable to acting ethically.
**6.05. Not promote their own interest at the expense of the profession, client or employer.**

6.06. Obey all laws governing their work, unless, in exceptional circumstances, such compliance is inconsistent with the public interest.
6.08. Take responsibility for detecting, correcting, and reporting errors in software and associated documents on which they work.
7.07. Not unfairly intervene in the career of any colleague; however, concern for the employer, the client or public interest may compel software engineers, in good faith, to question the competence of a colleague.
8.07 Not give unfair treatment to anyone because of any irrelevant prejudices.
## Cheryl
- similar to Sam but not as severe as she is dissatisfied but did not think to actually sabotage  
# 3. Report on a Software Disaster


https://www.nerc.com/search/Pages/results.aspx?k=blackout
https://www.nerc.com/pa/rrm/ea/August%2014%202003%20Blackout%20Investigation%20DL/NERC_Final_Blackout_Report_07_13_04.pdf#search=blackout
- page 32
https://www.nerc.com/pa/rrm/ea/August%2014%202003%20Blackout%20Investigation%20DL/Blackout-OneYearLater(PRINT).pdf#search=blackout

https://sma.nasa.gov/docs/default-source/safety-messages/safetymessage-2008-03-01-northeastblackoutof2003.pdf
- page 3

https://www.theregister.com/2004/04/08/blackout_bug_report/
> Sometimes working late into the night and the early hours of the morning, the team pored over the approximately one-million lines of code that comprise the XA/21's Alarm and Event Processing Routine, written in the C and C++ programming languages. Eventually they were able to reproduce the Ohio alarm crash in GE Energy's Florida laboratory, says Unum. "It took us a considerable amount of time to go in and reconstruct the events." In the end, they had to slow down the system, injecting deliberate delays in the code while feeding alarm inputs to the program. About eight weeks after the blackout, the bug was unmasked as a particularly subtle incarnation of a common programming error called a "race condition," triggered on August 14th by a perfect storm of events and alarm conditions on the equipment being monitoring. The bug had a window of opportunity measured in milliseconds.
> 
> "There was a couple of processes that were in contention for a common data structure, and through a software coding error in one of the application processes, they were both able to get write access to a data structure at the same time," says Unum. "And that corruption lead to the alarm event application getting into an infinite loop and spinning."
https://www.theregister.com/2004/02/12/software_bug_contributed_to_blackout/

https://www.energy.gov/sites/prod/files/oeprod/DocumentsandMedia/BlackoutFinal-Web.pdf
- loss of Eastlike 5 unit in Cleveland Ohio
- system unable to sustain additional load
- At no time during the morning or early afternoon of August 14 did the FE operators indicate voltage problems or request any assistance from outside the FE control area for voltage support. FE did not report the loss of Eastlake Unit 5 to MISO. Further, MISO did not monitor system voltages; that responsibility was left to its member operating systems
- powers was transfered to other lines in the Cleveland area

- At 14:02 EDT, Dayton Power & Light’s (DPL) Stuart-Atlanta 345-kV line tripped off-line due to a tree contact
- Affected MISO's state estimator that was supposed to run every 30 mins, unable to assess system conditions, which determined if contingency analyses performed
	- known problems with automatic analysis since installation in 1995
	- practice was for manual runs
	- no operators ran contingency analysis after loss of either, for the whole day
	- https://www.nerc.com/pa/rrm/ea/August%2014%202003%20Blackout%20Investigation%20DL/NERC_Final_Blackout_Report_07_13_04.pdf#search=blackout page 35
- 14:14, 
___
- system operators unaware of major system malfunction
	- https://www.nerc.com/pa/rrm/ea/August%2014%202003%20Blackout%20Investigation%20DL/NERC_Final_Blackout_Report_07_13_04.pdf#search=blackout
	-  https://sma.nasa.gov/docs/default-source/safety-messages/safetymessage-2008-03-01-northeastblackoutof2003.pdf
	- https://www.theregister.com/2004/02/12/software_bug_contributed_to_blackout/
	- unable to respond in time 
- XA/21 race condition GE Energy Management System
	- https://www.theregister.com/2004/04/08/blackout_bug_report/
- FirstEnergy coordination center knew of the system crashes but not able to warn local operators due to diagnostic system problems
	- https://sma.nasa.gov/docs/default-source/safety-messages/safetymessage-2008-03-01-northeastblackoutof2003.pdf

___
- On August 14, 2003, North America experienced the largest power blackout to date. Affecting northeastern United States and southeastern Canada, a combined total of approximately 50 million people did not have electricity for around 30 hours.
	- https://www.cbc.ca/archives/the-great-north-america-blackout-of-2003-1.4683696
- Result of a bunch of disconnected issues that all happened at the same time
- https://sma.nasa.gov/docs/default-source/safety-messages/safetymessage-2008-03-01-northeastblackoutof2003.pdf

- On the physical infrastructure side, the whole issue started when the Eastlake 5 power station generator unit tripped and shut down when an operator increased power output above system protection thresholds.
	- https://www.energy.gov/sites/prod/files/oeprod/DocumentsandMedia/BlackoutFinal-Web.pdf
	- 2 of Cleveland's other units Davis-Besse and Eastlake 4 were already shut down for maintenence
- Sudden drop in voltage caused a major imbalance to Cleveland and Akron areas which subsequently caused transmission lines to sag and short-circuit with overgrown trees
- Continued with key Sammis-Star line which triggered more cascading failures with linked transmission lines in Northern US and Canada

- On a software side, the issues became as dire as it was due to a lack of operational awareness and system malfunctions
- Ultimately, it came down to two groups of related failures.
## MISO fail
- Started when inaccurate input data rendered the state estimator in the Midwestern Independent System Operator (MISO), FirstEnergy's (FE) regional coordination center being ineffective
	- This tool was responsible for assessing system conditions on a 5 minute interval and performing contingency analyses at a slower rate to predict behaviour and alert operator if the system was not in a balanced state
		- https://www.energy.gov/sites/prod/files/oeprod/DocumentsandMedia/BlackoutFinal-Web.pdf
	- Before the failing of the Eastlake 5 unit, the state estimator had issues with out-of-sync data (due to an outage on Cinergy's Bloomington-Denois Creek line) which caused information to be mis-matched outside of the acceptable error bounds. An analyst was called to fix the issue, who turned off the automatic trigger function for troubleshooting, but forgot to re-enable the 5-minute schedule afterwards. The state estimator was fully back in operation only moments before the start of the major cascading failures.
		- https://www.energy.gov/sites/prod/files/oeprod/DocumentsandMedia/BlackoutFinal-Web.pdf
	- As a result, the state estimator was unable to determine that with Eastlake 5 down, other transmissions would overload in correspondence
		- https://www.energy.gov/sites/prod/files/oeprod/DocumentsandMedia/BlackoutFinal-Web.pdf
	- Even without the de-sync error at the time, FirstEnergy indicated problems with the automatic contingency analysis operation since installation in 1995, so the standard practice was to manually run the analysis as needed
		-  https://www.nerc.com/pa/rrm/ea/August%2014%202003%20Blackout%20Investigation%20DL/NERC_Final_Blackout_Report_07_13_04.pdf#search=blackout
	- It is worth noting that FirstEnergy operators did not manually access contingency analysis results at any time during the day on August 14
		- https://www.nerc.com/pa/rrm/ea/August%2014%202003%20Blackout%20Investigation%20DL/NERC_Final_Blackout_Report_07_13_04.pdf#search=blackout
	- The lack of situational awareness from the operators in investigating and notifying others escalated the issue as other facilities were unaware of the overall problem due to little communication and dealing with their own system failures at the time
## Control Room fail
- Within the time frame when MISO's state estimator was down, FirstEnergy's control room lost audio and visual alarm functionality on their Energy Management System (EMS) which indicated when equipment entered critical condition.
	- https://www.energy.gov/sites/prod/files/oeprod/DocumentsandMedia/BlackoutFinal-Web.pdf
- The FE operator heavily relied on the alarm processor as there did not exist other prominent visualizations. There did not exist any periodic diagnostics for this system to indicate the failure.
	- https://www.energy.gov/sites/prod/files/oeprod/DocumentsandMedia/BlackoutFinal-Web.pdf
- Had they known of the failure, they would have known to more closely monitor the numerical data they received, scanning through numerous data points across multiple screens.
	- https://www.energy.gov/sites/prod/files/oeprod/DocumentsandMedia/BlackoutFinal-Web.pdf
- At this point the EMS system had stalled, crashing the main server, and subsequently the backup server as the failing alarm system causing the issue was copied over. This silently slowed information refresh from intervals from 1 to 3 seconds to a refresh rate of every 59 seconds.
	- https://www.energy.gov/sites/prod/files/oeprod/DocumentsandMedia/BlackoutFinal-Web.pdf page 62
- Although the alarm failed, the rest of the system continued to collect and send diagnostic data to other entities like MISO. The control room operators were thus confused as they received calls from other entities indicating on the critical event. However, the FE operators dismissed the information using the outdated system information they were viewing and at no time did they contact IT or other staff to confirm the situation.
- As a result, the FE operators did not recognize the events that were occurring, and was not able to stop the cascading damage.
	- https://www.nerc.com/pa/rrm/ea/August%2014%202003%20Blackout%20Investigation%20DL/NERC_Final_Blackout_Report_07_13_04.pdf#search=blackout
- It took eight weeks after the blackout to determine the cause of the alarm system failure as a race condition in the XA/21 EMS's "Alarm and Event Processing Routine" where multiple processes were in a deadlock for write access to a common data structure.
	- https://www.theregister.com/2004/04/08/blackout_bug_report/

- Overall, the issue spiraled out of control due a lack of communication and awareness from many parties involved as well as little preventative measures or checks for special circumstances.

- **TODO: continue with page 61~64 saying overloaded buffers, lack of comms from Computer support staff, outdated information compared to what they later received from other sources, both servers failing,**
	- also page 37 onwards for https://www.nerc.com/pa/rrm/ea/August%2014%202003%20Blackout%20Investigation%20DL/NERC_Final_Blackout_Report_07_13_04.pdf#search=blackout
	- use following for more info about race condition
		- https://www.theregister.com/2004/02/12/software_bug_contributed_to_blackout/
		- https://www.theregister.com/2004/04/08/blackout_bug_report/