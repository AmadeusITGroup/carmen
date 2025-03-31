### Community guidelines
 * Be respectful to others
 * Be appreciative and welcoming
 * Don't be judgmental
 * Be patient and supportive to newcomers
 * Value each contribution, even if it's not perfect - we can work as a team to benefit even from a failed attempt as we can learn from it!
 * Look after one another - we are community of like-minded people who care about others, not only about ticking the boxes
 * A challenge is not a bad thing, as it leads to expanding the horizons, being to competitive leads to unhealthy situations - be reasonable here

### Code conventions
Please follow the standard python rules if possible:
  * existing conventions
  * [PEP8](https://www.python.org/dev/peps/pep-0008/)
  * [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

There is always room for opportunistic refactoring, but be careful and ensure the cosmetic changes have no adverse impact on performance or readability.

### Testing conventions
The project comes which a suite of unit tests covering most of the aspects. Make sure you pass all the existing tests locally before submitting the PR. Furthermore, any new feature, flow or the amendment of the existing one should be reflected in newly added unit tests or the update of the existing tests depending on the context.

Please follow [pytest good practices](https://docs.pytest.org/en/stable/goodpractices.html). You can also draw some inspirations from [this article](https://realpython.com/pytest-python-testing/).

Make sure you test the syntax before submitting the PR. Run a local build if you can and verify if all the new extra resources are also checked in.

### Branching conventions
We are working with a single master branch and one release branch to make is simple.

### Commit-message conventions
 * Prefix each commit with the Jira/GitHub Issue ticket number if possible i.e. [ABC-123] New package nnn added to allow running bbb
 * Provide a high level summary of the changes. Try to be concise.
 * Make the commit messages meaningful. Don't skip them. They may be helpful during the code review and act as a passive documentation going forwards.

### Steps for creating good pull requests
  * State your intent is very clearly
  * If there is a need to provide a thorough explanation or refer to external sources, please do it - it will help in the review
  * Use the Jira/GitHub Issue ticket as a prefix in the PR title to ensure we get nice cross-references
  * If you are unsure about certain aspects, don't be scared of asking on the available forums ahead of creating the PR.
  * If you are aware of some drawback of the changes introduced be transparent about it, the reviewers will weigh pros and cons and your contribution may still be accepted
  * To stick to a reasonable number of commits in your PR, you  may want to squash some of them using [the git  history rewriting technique](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)
  * You can use the PR as a medium for the conversation between  yourself and the project maintainers. You can prefix the PR with a meaningful tag eg. [IDEA], [SUGGESTION], [REMARK] etc. In such case your PR may never be integrated if what you are proposing is not in line with the general direction the project is going to. However, it would be still a valuable resource to track the discussion that took place and it may save time for somebody who is heading in a similar direction.

### Expected timelines(SLAs) for the code review and the integration
 * The PRs should be reviewed within 1 week at least
 * The integration happens immediately after the PR is approved and merged into the target branch 

### How to submit feature requests
 * You may want to discuss the feature on the teams channel or other forums availabe for the project
 * Use Jra board or GitHub Issues associated to this project
 * Link the PR(when the contribution is planned) with the Jira ticket/GitHub issue if possible - it may give us more context and will make the case for the change stronger
 * Please be thorough with the description
 * Highlight a reasonable timescale you wish the feature to be integrated within - it is helpful when prioritizing 

### How to submit bug reports
 * Check carefully the documentaion and by asking on the available forums if the behaviour you are experiencing is expected or if it is a bug
 * Use Issues board associated to the project
 * Link the PR(when the contribution is planned) with the bug report request if possible - it may give us more context
 * Please be thorough with the description
 * Highlight a reasonable timescale you wish the feature to be integrated within - it is helpful when prioritizing 

### How to submit security issue reports
* Engage with project maintainers. Do not publicly disclose anything before the patch is delivered.

### How to write documentation
  * README.md and GETTINGSTARTED.md are where we describe the overview, the usage and the development practices
  * Use [markdown syntax](https://www.markdownguide.org/basic-syntax/) which is widely supported in the GitHub, BitBucket WebUI as well as in many IDEs
  * Use plain English and check your spelling prior to committing the change
  * Remember that good documentation is essential, so take time to do it properly

### Dependencies
All the development dependencies are incorporated into [pyproject.toml](./pyproject.toml).

### Build process schedule
The deliverable(python wheel) is built as soon as the PR is created, modified or merged into release(main) branch.

### Sprint schedule
There is no specific scrum setup here. All the changes are worked on in a best effort mode.

### Road map
There is no roadmap yet. One will be created if there is a need for it.

### When the repositories will be closed to contributions
At this stage the repositories never get frozen.

### Time reporting
There is no budget behind this project. Potential contributors need to negotiate it with their line or project managers.

### Helpful links, information, and documentation
  * [Markdown syntax](https://www.markdownguide.org/basic-syntax/)
  * [PEP8](https://www.python.org/dev/peps/pep-0008/)
  * [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
