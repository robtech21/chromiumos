*** note
**IMPORTANT**: Do *not* make changes to full.xml in this repo. This repo
automatically syncs with the private manifest repo
<https://chrome-internal.googlesource.com/chromeos/manifest-internal>. If you do
not have access to the private repo, please ask a Googler to update the manifest
on your behalf.
The changes must be synced to the infra/config file
chromeos\_repos.star. Without this, the repo will never be picked up by CQ.
***

# Repo Groups
Repo is the tool that we use to manage our local checkouts. It parses the
manifest specified by the `default.xml` file. The name of the manifest can be
overridden using `-m`. One could also check out a subset of the manifest using
the repo `groups` feature. This section documents the important groups that are
part of the default chromiumos manifest.

## minilayout
This group is the minimum subset of repos needed to do a full build of Chrome
OS. It doesn't include all of the repos to necessarily test the OS image but
does include all those needed to create an image.

## buildtools
The subset of repos needed to perform release actions i.e. payload generation,
etc. Used by release engineers, TPMs, and Infra team members. Note this group
isn't useful without a checkout of manifest-internal.

## labtools
Tools needed to perform routine lab administrative actions like DUT
re-allocation or lab server management.
