"""Portal settings tests."""

from plone import api

import pytest


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    @pytest.mark.parametrize(
        "key,expected",
        [
            ["plone.site_title", "Intranet da Lactec"],
            ["plone.email_from_name", "Intranet da Lactec"],
            ["plone.smtp_host", "localhost"],
            ["plone.smtp_port", 25],
            ["plone.twitter_username", "lactec"],
            ["plone.facebook_username", "lactec"],
            ["plone.linkedin_username", "lactec"],
            ["plone.instagram_username", "lactec"],
            ["plone.youtube_username", "lactec"],
            ["plone.portal_timezone", "AMERICA/SAO_PAULO"],
            ["plone.default_language", "pt-br"],
            ["plone.available_languages", ["pt-br", "en"]],
            ["plone.use_email_as_login", False],
        ],
    )
    def test_setting(self, portal, key: str, expected: str | int):
        """Test registry setting."""
        value = api.portal.get_registry_record(key)
        assert value == expected
