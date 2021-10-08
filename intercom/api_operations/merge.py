class Merge(object):
    """A mixin that provides `merge` functionality."""

    def merge(self, from_lead, into_user):
        """Merge the specified contact lead into the specified contact user."""
        self.client.post(
            '/contacts/merge',
            {
                'from': from_lead.id,
                'into': into_user.id,
            }
        )
