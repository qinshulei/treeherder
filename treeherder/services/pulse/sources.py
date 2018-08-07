import environ

env = environ.Env()


exchanges = env.list("PULSE_JOB_EXCHANGES", default=[
    "exchange/taskcluster-treeherder/v1/jobs",
    # "exchange/fxtesteng/jobs",
    # ... other CI systems
])
projects = env.list("PULSE_JOB_PROJECTS", default=[
    "#",
    # some specific repos TC can ingest from
    # "mozilla-central.#",
    # "mozilla-inbound.#",
])


def get_job_sources():
    """
    Get Job ingestion source locations.

    Specifies the Pulse exchanges Treeherder will ingest data from for Jobs.
    This list will be updated as new applications come online that Treeherder
    supports.  Treeherder will subscribe with routing keys that are the project
    names.  Wildcards such as ``#`` and ``*`` are supported for the project
    field.
    """
    for exchange in exchanges:
        yield {
            "exchange": exchange,
            "projects": projects,
        }


def get_push_sources():
    """
    Get Push ingestion source locations.

    Specifies the Pulse exchanges Treeherder will ingest data from for Push
    data.
    """
    sources = env.json(
        "PULSE_PUSH_SOURCES",
        default=[{
            "exchange": "exchange/taskcluster-github/v1/push",
            "routing_keys": ['#'],
        }, {
            "exchange": "exchange/taskcluster-github/v1/pull-request",
            "routing_keys": ['#'],
        }, {
            "exchange": "exchange/hgpushes/v1",
            "routing_keys": ["#"]
        }],
    )

    return sources


job_sources = list(get_job_sources())
push_sources = get_push_sources()
