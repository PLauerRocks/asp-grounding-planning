#! /usr/bin/env python

import os
import platform

from lab.environments import LocalEnvironment, BaselSlurmEnvironment
from lab.experiment import Experiment

from downward import suites
from downward.reports.absolute import AbsoluteReport
from downward.reports.scatter import ScatterPlotReport

from common_setup import Configuration


from pathlib import Path

# Create custom report class with suitable info and error attributes.
class BaseReport(AbsoluteReport):
    INFO_ATTRIBUTES = []
    ERROR_ATTRIBUTES = [
        'domain', 'problem', 'algorithm', 'unexplained_errors', 'error', 'node']

NODE = platform.node()
REMOTE = NODE.endswith(".scicore.unibas.ch") or NODE.endswith(".cluster.bc2.ch")
BENCHMARKS_DIR = os.environ["DOWNWARD_BENCHMARKS"]
RUN_SCRIPT_DIR = str(Path(os.getcwd()).parent.parent)

if REMOTE:
    SUITE = ['agricola-opt18-strips', 'agricola-sat18-strips', 'airport', 'airport-adl', 'assembly', 'barman-mco14-strips', 'barman-opt11-strips', 'barman-opt14-strips', 'barman-sat11-strips', 'barman-sat14-strips', 'blocks', 'caldera-opt18-adl', 'caldera-sat18-adl', 'caldera-split-opt18-adl', 'caldera-split-sat18-adl', 'cavediving-14-adl', 'childsnack-opt14-strips', 'childsnack-sat14-strips', 'citycar-opt14-adl', 'citycar-sat14-adl', 'data-network-opt18-strips', 'data-network-sat18-strips', 'depot', 'driverlog', 'elevators-opt08-strips', 'elevators-opt11-strips', 'elevators-sat08-strips', 'elevators-sat11-strips', 'flashfill-sat18-adl', 'floortile-opt11-strips', 'floortile-opt14-strips', 'floortile-sat11-strips', 'floortile-sat14-strips', 'freecell', 'ged-opt14-strips', 'ged-sat14-strips', 'grid', 'gripper', 'hiking-agl14-strips', 'hiking-opt14-strips', 'hiking-sat14-strips', 'logistics00', 'logistics98', 'maintenance-opt14-adl', 'maintenance-sat14-adl', 'miconic', 'miconic-fulladl', 'miconic-simpleadl', 'movie', 'mprime', 'mystery', 'no-mprime', 'no-mystery', 'nomystery-opt11-strips', 'nomystery-sat11-strips', 'nurikabe-opt18-adl', 'nurikabe-sat18-adl', 'openstacks', 'openstacks-agl14-strips', 'openstacks-opt08-adl', 'openstacks-opt08-strips', 'openstacks-opt11-strips', 'openstacks-opt14-strips', 'openstacks-sat08-adl', 'openstacks-sat08-strips', 'openstacks-sat11-strips', 'openstacks-sat14-strips', 'openstacks-strips', 'optical-telegraphs', 'organic-synthesis-opt18-strips', 'organic-synthesis-sat18-strips', 'organic-synthesis-split-opt18-strips', 'organic-synthesis-split-sat18-strips', 'parcprinter-08-strips', 'parcprinter-opt11-strips', 'parcprinter-sat11-strips', 'parking-opt11-strips', 'parking-opt14-strips', 'parking-sat11-strips', 'parking-sat14-strips', 'pathways', 'pathways-noneg', 'pegsol-08-strips', 'pegsol-opt11-strips', 'pegsol-sat11-strips', 'petri-net-alignment-opt18-strips', 'philosophers', 'pipesworld-notankage', 'pipesworld-tankage', 'psr-large', 'psr-middle', 'psr-small', 'rovers', 'satellite', 'scanalyzer-08-strips', 'scanalyzer-opt11-strips', 'scanalyzer-sat11-strips', 'schedule', 'settlers-opt18-adl', 'settlers-sat18-adl', 'snake-opt18-strips', 'snake-sat18-strips', 'sokoban-opt08-strips', 'sokoban-opt11-strips', 'sokoban-sat08-strips', 'sokoban-sat11-strips', 'spider-opt18-strips', 'spider-sat18-strips', 'storage', 'termes-opt18-strips', 'termes-sat18-strips', 'tetris-opt14-strips', 'tetris-sat14-strips', 'thoughtful-mco14-strips', 'thoughtful-sat14-strips', 'tidybot-opt11-strips', 'tidybot-opt14-strips', 'tidybot-sat11-strips', 'tpp', 'transport-opt08-strips', 'transport-opt11-strips', 'transport-opt14-strips', 'transport-sat08-strips', 'transport-sat11-strips', 'transport-sat14-strips', 'trucks', 'trucks-strips', 'visitall-opt11-strips', 'visitall-opt14-strips', 'visitall-sat11-strips', 'visitall-sat14-strips', 'woodworking-opt08-strips', 'woodworking-opt11-strips', 'woodworking-sat08-strips', 'woodworking-sat11-strips', 'zenotravel']
    ENV = BaselSlurmEnvironment(
        partition='infai_2',
        memory_per_cpu="6G",
        extra_options='#SBATCH --cpus-per-task=3',
        setup="%s\n%s" % (
            BaselSlurmEnvironment.DEFAULT_SETUP,
            "source /infai/blaas/virtualenvs/asp-grounding-planning/bin/activate\n"),
        export=["PATH", "DOWNWARD_BENCHMARKS", "POWER_LIFTED_DIR"])
else:
    SUITE = ['gripper:prob01.pddl',
             'miconic:s1-0.pddl']
    ENV = LocalEnvironment(processes=4)

TIME_LIMIT = 1800
MEMORY_LIMIT = 16384

ATTRIBUTES=['ground',
            'total_time']

# Create a new experiment.
exp = Experiment(environment=ENV)

# Add custom parser for Power Lifted.
exp.add_parser('parser.py')

CONFIGS = [Configuration('ground-actions', ['--ground-actions']),
           Configuration('not-ground-actions', [])]

# Create one run for each instance and each configuration
for config in CONFIGS:
    for task in suites.build_suite(BENCHMARKS_DIR, SUITE):
        run = exp.add_run()
        run.add_resource('domain', task.domain_file, symlink=True)
        run.add_resource('problem', task.problem_file, symlink=True)
        run.add_command('run-search',
                        [RUN_SCRIPT_DIR+'/generate-asp-model.py', '-i', task.problem_file,
                         '-m', '{}-{}-{}.model'.format(config.name, task.domain, task.problem),
                         '-t', '{}-{}-{}.theory'.format(config.name, task.domain, task.problem)] + config.arguments,
                        time_limit=TIME_LIMIT,
                        memory_limit=MEMORY_LIMIT)
        run.set_property('domain', task.domain)
        run.set_property('problem', task.problem)
        run.set_property('algorithm', config.name)
        run.set_property('id', [config.name, task.domain, task.problem])

        # Add step that writes experiment files to disk.
exp.add_step('build', exp.build)

# Add step that executes all runs.
exp.add_step('start', exp.start_runs)

# Add step that collects properties from run directories and
# writes them to *-eval/properties.
exp.add_fetcher(name='fetch')

def remove_timeouts(run):
    if 'total_time' in run:
        if run['total_time'] > 1780:
            run['ground'] = 0
            run['total_time'] = None
    return run

# Make a report.
exp.add_report(
    BaseReport(attributes=ATTRIBUTES, filter=remove_timeouts),
    outfile='report.html')

# Parse the commandline and run the specified steps.
exp.run_steps()
