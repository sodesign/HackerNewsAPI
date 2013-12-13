from hn import HN
from nose import with_setup

class Test_Stories_Dict(object):
    
    @classmethod
    def setup(self):
        self.hn = HN()
        self.top_stories = self.hn.get_stories()
        self.newest_stories = self.hn.get_stories(story_type='newest')
        self.best_stories = self.hn.get_stories(story_type='best')
    
    @classmethod
    def teardown(self):
        pass
    
    
    @with_setup(setup, teardown)
    def test_stories_dict_structure_top(self):
        """
        Checks data type of each field of each story from front page.
        """
        for story in self.top_stories:
            # testing for unicode or string
            # because the types are mixed sometimes
            assert type(story['rank']) == int
            assert type(story['story_id']) == int
            assert type(story['title']) in [unicode, str]
            assert type(story['link']) in [unicode, str]
            assert type(story['domain']) in [unicode, str]
            assert type(story['points']) == int
            assert type(story['submitter']) in [unicode, str]
            assert type(story['published_time']) in [unicode, str]
            assert type(story['submitter_profile']) in [unicode, str]
            assert type(story['num_comments']) == int
            assert type(story['comments_link']) in [unicode, str]
            assert type(story['is_self']) == bool
    
    @with_setup(setup, teardown)
    def test_stories_dict_structure_newest(self):
        """
        Checks data type of each field of each story from newest page
        """
        for story in self.newest_stories:
            # testing for unicode or string
            # because the types are mixed sometimes
            assert type(story['rank']) == int
            assert type(story['story_id']) == int
            assert type(story['title']) in [unicode, str]
            assert type(story['link']) in [unicode, str]
            assert type(story['domain']) in [unicode, str]
            assert type(story['points']) == int
            assert type(story['submitter']) in [unicode, str]
            assert type(story['published_time']) in [unicode, str]
            assert type(story['submitter_profile']) in [unicode, str]
            assert type(story['num_comments']) == int
            assert type(story['comments_link']) in [unicode, str]
            assert type(story['is_self']) == bool
    
    @with_setup(setup, teardown)
    def test_stories_dict_structure_best(self):
        """
        Checks data type of each field of each story from best page
        """
        for story in self.best_stories:
            # testing for unicode or string
            # because the types are mixed sometimes
            assert type(story['rank']) == int
            assert type(story['story_id']) == int
            assert type(story['title']) in [unicode, str]
            assert type(story['link']) in [unicode, str]
            assert type(story['domain']) in [unicode, str]
            assert type(story['points']) == int
            assert type(story['submitter']) in [unicode, str]
            assert type(story['published_time']) in [unicode, str]
            assert type(story['submitter_profile']) in [unicode, str]
            assert type(story['num_comments']) == int
            assert type(story['comments_link']) in [unicode, str]
            assert type(story['is_self']) == bool
    
    @with_setup(setup, teardown)
    def test_stories_dict_length_top(self):
        """
        Checks if the dict returned by scraping the front page of HN is 30.
        """
        assert len(self.top_stories) == 30
    
    @with_setup(setup, teardown)
    def test_stories_dict_length_best(self):
        """
        Checks if the dict returned by scraping the best page of HN is 30.
        """
        assert len(self.best_stories) == 30
        
    @with_setup(setup, teardown)
    def test_stories_dict_length_top_newest(self):
        """
        Checks if the dict returned by scraping the newest page of HN is 30.
        """
        assert len(self.newest_stories) == 30