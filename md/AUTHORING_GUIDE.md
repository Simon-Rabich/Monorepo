# Python Sample Authoring Guide

 The guidelines below are intended to ensure that all Python samples
meet the following goals:

* **Copy-paste-runnable.** A developer should be able to copy and paste the
code into their own environment and run it with as few modifications as
possible.
* **Teach through code.** Each sample should demonstrate best practices for
interacting with Google Cloud libraries, APIs, or services.
* **Idiomatic.** Each sample should follow widely accepted Python best
practices as covered below.


## FAQs

### Where should I put my samples?

See [Folder Location](#folder-location). Samples live in this repository, **python-docs-samples**,
or in a library repository.

### Where are the client libraries?


### Who reviews my PR?

Please reach out to your assigned reviewer if it's been more than 2 days and you haven't gotten a response!

### How do I set up my environment?

You should install the latest patch version of each minor version listed in [Python Versions](#python-versions).

We recommend using the Python version management tool [Pyenv](https://github.com/pyenv/pyenv) if you are using MacOS or Linux.

**Googlers:** See [the internal Python policies doc](https://g3doc.corp.google.com/company/teams/cloud-devrel/dpe/samples/python.md?cl=head).

**Using MacOS?:** See [Setting up a Mac development environment with pyenv and pyenv-virtualenv](MAC_SETUP.md).

Afterwards, see [Test Environment Setup](#test-environment-setup).


## Sample Guidelines

This section covers guidelines for Python samples. Note that
[Testing Guidelines](#testing-guidelines) are covered separately below.

### Python Versions

Samples should support Python 3.6, 3.7, 3.8, and 3.9.

If the API or service your sample works with has specific Python version
requirements different from those mentioned above, the sample should support
those requirements.

### License Header

Source code files should always begin with an Apache 2.0 license header. See
the instructions in the repo license file on [how to apply the Apache license
to your work](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/LICENSE#L178-L201).
For example, see the license header for the [Datastore client quickstart
sample](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/datastore/cloud-client/quickstart.py#L1-L15).

### Shebang

If, and only if, your sample application is a command-line application, then
include a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) as the
first line. Separate the shebang line from the rest of the application with
a blank line. The shebang line for a Python application should always be:

```python
#!/usr/bin/env python
```

Don't include shebang lines in web applications or test files.

### Coding Style

All Python samples should follow the best practices defined in the
[PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/) and the
[Google Python Style Guide](http://google.github.io/styleguide/pyguide.html).
The automated linting process for Python samples uses
[flake8](http://flake8.pycqa.org/en/latest/) to verify conformance to common
Python coding standards, so the use of flake8 is recommended.

If you prefer to use [pylint](https://www.pylint.org/), note that Python
samples for this repo are not required to conform to pylint’s default settings
outside the scope of PEP 8, such as the “too many arguments” or “too many
local variables” warnings.

The use of [Black](https://pypi.org/project/black/) to standardize code
formatting and simplify diffs is recommended, but optional.

The default noxfile has `blacken` session for convenience. Here are
some examples.

If you have pyenv configured:
```sh
nox -s blacken
```

If you only have docker:
```
cd proj_directory
../scripts/run_tests_local.sh . blacken
```

In addition to the syntax guidelines covered in PEP 8, samples should strive
to follow the Pythonic philosophy outlined in the
[PEP 20 - Zen of Python](https://www.python.org/dev/peps/pep-0020/) as well
as the readability tenets presented in Donald Knuth's
_[Literate Programming](https://en.wikipedia.org/wiki/Literate_programming)_.
Notably, your sample program should be self-contained, readable from top to
bottom, and fairly self-documenting. Prefer descriptive names, and use
comments and docstrings only as needed to further clarify the code’s intent.


### Functions and Classes

Very few samples will require authoring classes. Prefer functions whenever
possible. See [this video](https://www.youtube.com/watch?v=o9pEzgHorH0) for
some insight into why classes aren't as necessary as you might think in Python.
Classes also introduce cognitive load. If you do write a class in a sample, be
prepared to justify its existence during code review.

#### Descriptive function names

Always prefer descriptive function names, even if they are long.
For example `upload_file`, `upload_encrypted_file`, and `list_resource_records`.
Similarly, prefer long and descriptive parameter names. For example
`source_file_name`, `dns_zone_name`, and `base64_encryption_key`.

Here's an example of a top-level function in a command-line application:

```python
def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs()

    for blob in blobs:
        print(blob.name)
```

Notice the simple docstring and descriptive argument name (`bucket_name`
implying a string instead of just `bucket` which could imply a class instance).

This particular function is intended to be the "top of the stack" - the function
executed when the command-line sample is run by the user. As such, notice that
it prints the blobs instead of returning. In general, top of the stack
functions in command-line applications should print, but use your best
judgment.

#### Documenting arguments

Here's an example of a more complicated top-level function in a command-line
application:

```python
def download_encrypted_blob(
        bucket_name, source_blob_name, destination_file_name,
        base64_encryption_key):
    """Downloads a previously-encrypted blob from Google Cloud Storage.

    The encryption key provided must be the same key provided when uploading
    the blob.
    """
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    # Encryption key must be an AES256 key represented as a bytestring with
    # 32 bytes. Since it's passed in as a base64 encoded string, it needs
    # to be decoded.
    encryption_key = base64.b64decode(base64_encryption_key)

    blob.download_to_filename(
        destination_file_name, encryption_key=encryption_key)

    print(f'Blob {source_blob_name} downloaded to {destination_file_name}.'
```

Note the verbose parameter names and the extended description that helps the
user form context. If there were more parameters or if the parameters had
complex context, then it might make sense to expand the docstring to include
an `Args` section such as:

```
Args:
    bucket_name: The name of the cloud storage bucket.
    source_blob_name: The name of the blob in the bucket to download.
    destination_file_name: The blob will be downloaded to this path.
    base64_encryption_key: A base64-encoded RSA256 encryption key. Must be the
        same key used to encrypt the file.
```

Generally, however, it's rarely necessary to exhaustively document the
parameters this way. Lean towards unsurprising arguments with descriptive
names, as having to resort to this kind of docstring might be extremely
accurate but it comes at the cost of high redundancy, signal-to-noise ratio,
and increased cognitive load.

#### Documenting types

Argument types should be documented using Python type annotations as
introduced in [PEP 484](https://www.python.org/dev/peps/pep-0484/). For example:

```py
def hello_world(name: str) -> None:
    print(f"Hello {name}!")
```

```py
def adder(a: int, b: int) -> int:
    return a+b
```

Type hinting is enforced using [`flake8-annotations`](https://pypi.org/project/flake8-annotations/), which is enabled by setting the `enforce_type_hints` variable to `True` in the appropriate `noxfile_config.py`. Type hinting is expected in all new samples, and will gradually be added to all compatible existing samples.

If there is an `Args` section within the function's docstring, consider
documenting the argument types there as well. For example:

```
Args:
    credentials (google.oauth2.credentials.Credentials): Credentials
      authorized for the current user.
```

When documenting primitive types, be sure to note if they have a particular set
of constraints. For example, `A base64-encoded string` or `Must be between 0
and 10`.

### `datetime.datetime` Objects

Always create timezone aware datetime objects. For libraries that use protobuf,
omitting the timezone may lead to unexpected behavior when the datetime
is converted to a protobuf timestamp.

```py
import datetime

now = datetime.datetime.now(tz=datetime.timezone.utc)
```

For more information see the [Python datetime documentation](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcfromtimestamp).

### README File

Each sample should have a `README.md` file that provides instructions for how
to install, configure, and run the sample. Setup steps that cover creating
Google Cloud projects and resources should link to appropriate pages in the
[Google Cloud Documentation](https://cloud.google.com/docs/), to avoid
duplication and simplify maintenance.

### Dependencies

Every sample should include a
[requirements.txt](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
file that lists all of its dependencies, to enable others to re-create the
environment that was used to create and test the sample. All dependencies
should be pinned to a specific version, as in this example:

```
Flask==1.1.1
PyMySQL==0.9.3
SQLAlchemy==1.3.12
```

If a sample has testing requirements that differ from its runtime requirements
(such as dependencies on [pytest](http://pytest.org/en/latest/) or other
testing libraries), the testing requirements may be listed in a separate
`requirements-test.txt` file instead of the main `requirements.txt` file.

#### Developing samples for un-released changes

Pip has [VCS support](https://pip.pypa.io/en/stable/cli/pip_install/#vcs-support). Use the branch name or commit hash instead of the package name.


**pip install**:
```
pip install git+https://github.com/googleapis/python-firestore.git@ee518b741eb5d7167393c23baa1e29ace861b253
```

**requirements.txt**:
```
Flask==1.1.1
PyMySQL==0.9.3
git+https://github.com/googleapis/python-firestore.git@ee518b741eb5d7167393c23baa1e29ace861b253
```


### Region Tags

Sample code may be integrated into Google Cloud Documentation through the use
of region tags, which are comments added to the source code to identify code
blocks that correspond to specific topics covered in the documentation. For
example, see
[this sample](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/cloud-sql/mysql/sqlalchemy/main.py)
— the region tags are the comments that begin with `[START` or `[END`.

The use of region tags is beyond the scope of this document, but if you’re
using region tags they should start after the source code header
(license/copyright information), but before imports and global configuration such as
initializing constants.

### Exception Handling

Sample code should use standard Python exception handling techniques as
covered in the [Google Python Style
Guide](http://google.github.io/styleguide/pyguide.html#24-exceptions).

## Testing Guidelines

Samples should include tests to verify that the sample runs correctly and
generates the intended output. Follow these guidelines while writing your
tests:

* Use [pytest](https://docs.pytest.org/en/latest/)-style tests and plain
asserts. Don't use `unittest`-style tests or `assertX` methods.
* Whenever possible, tests should allow for future changes or additions to
APIs that are unrelated to the code being tested.
For example, if a test is intended to verify a JSON payload
returned from an endpoint, it should only check for the existence of the
expected keys and values, and the test should continue to work correctly
if the order of keys changes or new keys are added to the response in a future
version of the API. In some cases, it may make sense for tests to simply
verify that an API call was successful rather than checking the response
payload.
* Samples that use App Engine Standard should use the [App Engine
testbed](https://cloud.google.com/appengine/docs/standard/python/refdocs/google.appengine.ext.testbed)
for system testing, as shown in [this
example](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/appengine/standard/localtesting/datastore_test.py).
* All tests should be independent of one another and order-independent.
* We use parallel processing for tests, so tests should be capable of running in parallel with one another.
* Use pytest's fixture for resource setup and teardown, instead of
  having them in the test itself.
* Avoid infinite loops.
* Retry RPCs
* You can enable running tests in parallel by adding `pytest-parallel` or `pytest-xdist`
  to your `requirements-test.txt` file.

### Arrange, Act, Assert

Tests for samples should follow the “Arrange, Act, Assert” structure:

* _Arrange_ — create and configure the components required for the test.
Avoid nesting; prioritize readability and simplicity over efficiency. For
Python tests, typical "arrange" steps include imports, copying environment
variables to local variables, and so on.
* _Act_ — execute the code to be tested, such as sending a request to an API and
receiving a response.
* _Assert_ — verify that the test results match what is expected, using an
`assert` statement.

### External Resources

Whenever possible, tests should run against the live production version of
cloud APIs and resources. This will assure that any breaking changes in those
resources are identified by the tests.

External resources that must exist prior to the test (for example, a
Cloud SQL instance) should be identified and passed in through an environment
variable. If specific data needs to exist within such infrastructure resources,
however, the test should create this data as part of its _Arrange_ steps and
then clean up when the test is completed.

Creating mocks for external resources is strongly discouraged. Tests should
verify the validity of the sample against the APIs, and not against a mock
that embodies assumptions about the behavior of the APIs.

### Temporary Resources

When tests need temporary resources (such as a temp file or folder), they
should create reasonable names for these resources with a UUID attached to
assure uniqueness. Use the Python ```uuid``` package from the standard
library to generate UUIDs for resource names. For example:

```python
glossary_id = f'test-glossary-{uuid.uuid4()}'
```

or:

```python
# If full uuid4 is too long, use its hex representation.
encrypted_disk_name = f'test-disk-{uuid.uuid4().hex}'
```

```python
# If the hex representation is also too long, slice it.
encrypted_disk_name = f'test-disk-{uuid.uuid4().hex[:5]}'
```

All temporary resources should be explicitly deleted when testing is
complete. Use pytest's fixture for cleaning up these resouces instead
of doing it in test itself.

We recommend using `finally` to ensure that resource deletion occurs even if there is an error on creation. For example, this fixture creates a Dataproc cluster and tears it down regardless of errors during creation.

```python
@pytest.fixture(scope="function")
def setup_and_teardown_cluster():
    try:
        # Create cluster using cluster client
        cluster_client = dataproc.ClusterControllerClient(
            client_options={
                "api_endpoint": f"{CLUSTER_REGION}-dataproc.googleapis.com:443"
            }
        )

        operation = cluster_client.create_cluster(
            project_id=PROJECT_ID, region=CLUSTER_REGION, cluster=CLUSTER_CONFIG
        )

        # Wait for cluster to provision
        operation.result()

        yield
    finally:
        try:
            # Delete cluster
            operation = cluster_client.delete_cluster(
                project_id=PROJECT_ID, region=CLUSTER_REGION, cluster_name=DATAPROC_CLUSTER
            )
            operation.result()
        except NotFound:
            print("Cluster already deleted")
```

### Console Output

If the sample prints output to the console, the test should capture stdout to
a file and verify that the captured output contains the key information that
is expected. Strive to verify the content of the output rather than the syntax.
For example, the test might verify that a string is included in the output,
without taking a dependency on where that string occurs in the output.

### Avoid infinite loops

Never put potential infinite loops in the test code path. A typical
example is about gRPC's LongRunningOperations. Make sure you pass the
timeout parameter to the `result()` call.

Good:

```python
# will raise google.api_core.GoogleAPICallError after 60 seconds
operation.result(60)
```

Bad:

```python
operation.result()  # this could wait forever.
```

We recommend the timeout parameter to be around the number that gives
you more than 90% success rate. Don't put too long a timeout.

Now this test is inevitably flaky, so consider marking the test as
`flaky` as follows:

```python

@pytest.mark.flaky(max_runs=3, min_passes=1)
def my_flaky_test():
    # test that involves LRO poling with the timeout
```

This combination will give you very high success rate with fixed test
execution time (0.999 success rate and 180 seconds operation wait time
in the worst case in this example).


### Test Environment Setup

You can easily `source` this file for exporting the environment variables.

#### Development environment setup

This repository supports two ways to run tests locally.

1. Docker

    This is another way of running the tests. Setup is easier because
    you only need to instal Docker. The test execution will be bit
    slower than the first one. This option is also useful if you need
    to simulate the CI system.


### Running tests 

Sample tests are run through [pytest](https://pytest.org).
[unittest](https://docs.python.org/3/library/unittest.html).


### Running tests with Docker

__Note__: This is currently only available for samples in `python-docs-samples`.

If you have [Docker](https://www.docker.com) installed and runnable by
the local user, you can use `scripts/run_tests_local.sh` helper script
to run the tests.


#### Secrets


Secrets (e.g., project names, API keys, passwords) are kept in
Cloud Secret Manager.


## Debugging

### Can I use a debugger for samples?

Yes, you can use `pdb` or any Python debugger. For pdb, use `import pdb; pdb.set_trace()` (<3.7) or `breakpoint` (3.7+).
See https://docs.python.org/3/library/pdb.html.

### How do I do that in IntelliJ, VSCode, etc.?

These IDEs just inject the breakpoint above into the code, so it should work.
