*** note
**IMPORTANT**: Changes to this repo must also be made in the private manfest
repo <https://chrome-internal.googlesource.com/chromeos/manifest-internal>.
Automated sync between manifest-internal and manifest is not yet set up.
And, the changes must *also* be synced to the infra/config file
chromeos_repos.star. Without this, the repo will never be picked up by CQ.
***

# Repo Groups
Repo is the tool that we use to manage our local checkouts. It parses the
manifest specified by the `default.xml` file. The name of the manifest can be
ovverriden using `-m`. One could also check out a subset of the manifest using
the repo `groups` feature. This section documents the important groups that are
part of the default chromiumos manifest.

## minilayout
This group is the minimum subset of repos needed to do a full build of Chrome
OS. It doesn't include all of the repos to necessarily test the OS image but
does include all those needed to create an iamge.

## buildtools
The subset of repos needed to perform release actions i.e. payload generation,
etc. Used by release engineers, TPMs, and Infra team members. Note this group
isn't useful without a checkout of manifest-internal.

## labtools
Tools needed to perform routine lab administrative actions like DUT
re-allocation or lab server management.
