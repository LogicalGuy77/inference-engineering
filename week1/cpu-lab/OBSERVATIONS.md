1. Why did one worker show ~100% in pidstat, but only ~6.25% overall?

> One worker shows 100% in pidstat because it is fully utilizing one logical CPU. We have 16 logical CPUs, so overall utilization is about 6.25%.

2. Why did two workers sharing CPU 0 each get ~50% CPU and ~50% wait?

> Two workers sharing CPU 0 get about 50% CPU and 50% wait because both continuously need CPU time, and the scheduler gives them roughly equal turns.

3. What changed when you placed them on separate CPUs?

> When we place them on different CPUs, they no longer compete for the same logical CPU, so each can get close to 100%.

4. Where did the sleeping worker’s elapsed time go?

> Elapsed time went into sleeping. The process was neither executing nor ready and waiting for CPU time.

5. What different question does each tool answer: mpstat, pidstat, vmstat, and uptime?

> mpstat gives us CPU-wise utilization. pidstat gives us process-wise and thread-wise usage, CPU waiting, and context switches. vmstat gives us an overall system view. uptime tells us how long Linux has been running and shows its load averages.

6. Why shouldn’t you add the process and thread rows above?

> We can’t add those process and thread rows because they represent the same work: our process has only one thread.