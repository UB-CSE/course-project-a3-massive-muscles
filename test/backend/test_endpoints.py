#!/usr/bin/env python3

import json
import os
import sys
import tempfile
import unittest

_dir_ = os.path.dirname(os.path.realpath(__file__))
_root_ = os.path.join(_dir_, '..', '..')

sys.path.append(_root_)

import Application.statistics as _SAPI
from Application.app import create_app

app = create_app()
app.config['TESTING'] = True

# Hooks for every request
app.before_request(_SAPI.pre_req)
app.after_request(_SAPI.post_req)


class TestForumCreate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        cls.client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        os.close(cls.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_api_create_endpoint(self):
        res = self.client.post("/web/forum/api/create", data=json.dumps({}))
        self.assertEqual(res.status_code, 200)

    def test_api_create_post_endpoint(self):
        res = self.client.post("/web/forum/api/post", data=json.dumps({}))
        self.assertEqual(res.status_code, 200)

    def test_api_latest_threads(self):
        res = self.client.get("/web/forum/api/latest")
        self.assertEqual(res.status_code, 200)

    def test_forum_api_thread(self):
        res = self.client.get("/web/forum/api/thread/1")
        self.assertEqual(res.status_code, 200),

    def test_statistics(self):
        res = self.client.get("/web/api/statistics")
        self.assertEqual(res.status_code, 200),

    def test_user_statistics(self):
        res = self.client.get("/web/api/statistics/1")
        self.assertEqual(res.status_code, 200),

    def test_metrics(self):
        res = self.client.get("/web/api/metrics")
        self.assertEqual(res.status_code, 200),


if __name__ == '__main__':
    unittest.main()
