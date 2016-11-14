""" Testing Methods for the Set class. 


@author: Nathan Sprague
@version: 9/14
"""
import unittest
from array_set import Set

class SetTester(unittest.TestCase):
    """Test class for testing Set methods.  """

    def setUp(self):
        # This just creates an empty set that can be used in any test. 
        # Not very useful, just here to demonstrate the setUp method. 
        self.test_set = Set()


    #--------------------------------------------------
    # Tests for the constructors.
    #--------------------------------------------------
    def test_constructor_empty_length(self):
        # Just test to make sure that a newly created Set has length 0.
        self.assertEqual(len(self.test_set), 0)

    def test_constructor_iterable_length(self):
        large_set = Set(["a", 1, 2, 3, "b"])
        self.assertEqual(len(large_set), 5)
        
    def test_constructor_iterable_repeats_length(self):
        large_set = Set(["a", 1, "a", 2, 3, "b", 2])
        self.assertEqual(len(large_set), 5)
        
        
    #---------------------------------------------------
    # Tests for the add method.  These tests check to see
    # that the length is correct after elements are added
    #---------------------------------------------------
    def test_add_one_item_length(self):
        self.test_set.add("hello")
        self.assertEqual(len(self.test_set), 1)

    def test_add_two_different_items_length(self):
        self.test_set.add("hello")
        self.test_set.add("goodbye")
        self.assertEqual(len(self.test_set), 2)
        self.assertEqual(self.test_set, Set(["hello", "goodbye"]))

    def test_add_two_equal_items_length(self):
        self.test_set.add("hello")
        self.test_set.add("hello")
        self.assertEqual(len(self.test_set), 1)
        self.assertEqual(self.test_set, Set(["hello"]))

    def test_add_several_equal_items(self):
        num_items = 100
        items = range(num_items)

        # Add them once
        for i in items:
            self.test_set.add(i)

        # Add them again
        for i in items:
            self.test_set.add(i)

        self.assertEqual(len(self.test_set), num_items)
        self.assertEqual(self.test_set, Set(range(num_items)))
        
            
    #---------------------------------------------------
    # Tests for Contains
    #---------------------------------------------------
    def test_contains_empty(self):
        self.assertFalse("a" in self.test_set)

    def test_contains_not_In(self):
        large_set = Set([1, 2, 3, "a", "b", "c"])
        self.assertFalse("z" in large_set)

    def test_contains_In(self):
        # Make a set containing the ints 0-99...
        large_set = Set(range(100))
        
        # Make sure each one is in the set...
        for i in range(100):
            self.assertTrue(i in large_set)
        
    def test_contains_doesnt_modify(self):
        # Create two equal sets...
        large_set1 = Set(range(100))
        large_set2 = Set(range(100))
        
        # Call contains on the first. 
        for i in range(100):
            i in large_set1
            'z' in large_set1

        # Make sure they are still equal. THIS TESTS REQUIRES
        # THAT THE EQUAL METHOD HAS BEEN FINISHED. 
        self.assertEqual(large_set1, large_set2)


    #-------------------------------------------------
    # Tests for clear method. 
    #-------------------------------------------------
    def test_clear_empty(self):
        self.test_set.clear()
        self.assertEqual(len(self.test_set), 0)

    def test_clear_full(self):
        large_set = Set(["a", "b", "c", 1, 2, 3])
        large_set.clear()
        self.assertEqual(self.test_set, large_set)


    #-------------------------------------------------
    # Tests for __len__.
    # (Already tested in tests for constructors and add.)
    #-------------------------------------------------


    #-------------------------------------------------
    # Make some helper methods for creating disjoint, equal, 
    # not-equal but non-disjoint sets:
    #-------------------------------------------------
        
    def _make_equal_sets(self):
        large_set1 = Set(["a", "b", "c", 1, 2, 3])
        large_set2 = Set(["a", "b", "c", 1, 2, 3])
        return (large_set1, large_set2)

    def _make_intersecting_sets(self):
        large_set1 = Set(["a", "b", 1, 2, 3])
        large_set2 = Set(["a", "b", "c", 2, 3])
        return (large_set1, large_set2)

    def _make_strict_subsets(self):
        large_set1 = Set(["a", "c", 1, 3])
        large_set2 = Set(["a", "b", "c", 1, 2, 3])
        return (large_set1, large_set2)

    def _make_disjoint_sets(self): 
        large_set1 = Set(["a", "b", "c"])
        large_set2 = Set([1, 2, 3])
        return (large_set1, large_set2)
        

    #-------------------------------------------------
    # Tests for == and != 
    #-------------------------------------------------

    def test_equal_empty(self):
        self.assertTrue(Set() == Set())

    def test_equal_non_empty(self):
        nonEmpty = Set([1, 2, 3])
        self.assertFalse(self.test_set == nonEmpty)
        self.assertTrue(self.test_set != nonEmpty)

    def test_equal_subset(self):
        set1, set2 = self._make_strict_subsets()
        self.assertFalse(set1 == set2)
        self.assertTrue(set1 != set2)

    def test_equal_superset(self):
        set1, set2 = self._make_strict_subsets()
        self.assertFalse(set2 == set1)
        self.assertTrue(set2 != set1)

    def test_equal_equal(self):
        set1, set2 = self._make_equal_sets()
        self.assertTrue(set2 == set1)
        self.assertFalse(set2 != set1)

    def test_equal_out_of_order(self):
        set1 = Set([1, 2, 3])
        set2 = Set([3, 2, 1])
        self.assertTrue(set2 == set1)
        self.assertFalse(set2 != set1)

    def test_equal_intersecting(self):
        set1, set2 = self._make_intersecting_sets()
        self.assertFalse(set1 == set2)
        self.assertFalse(set2 == set1)
        self.assertTrue(set1 != set2)
        self.assertTrue(set2 != set1)

    def test_equal_disjoint(self):
        set1, set2 = self._make_disjoint_sets()
        self.assertFalse(set1 == set2)
        self.assertFalse(set2 == set1)
        self.assertTrue(set1 != set2)
        self.assertTrue(set2 != set1)

    def test_equal_non_Set(self):
        self.assertFalse(Set() == [])
        self.assertTrue(Set() != [])

    def test_equal_non_collection(self):
        self.assertFalse(Set() == 0)
        self.assertTrue(Set() != 0)


    #-------------------------------------------------
    # Tests for the isdisjoint method. 
    #-------------------------------------------------

    def test_empty_are_disjoint(self):
        self.assertTrue(Set().isdisjoint(Set()))

    def test_disjoint_true(self):
        set1, set2 = self._make_disjoint_sets()
        self.assertTrue(set1.isdisjoint(set2))
        self.assertTrue(set2.isdisjoint(set1))

    def test_disjoint_intersecting(self):
        set1, set2 = self._make_intersecting_sets()
        self.assertFalse(set1.isdisjoint(set2))
        self.assertFalse(set2.isdisjoint(set1))

    def test_disjoint_subsets(self):
        set1, set2 = self._make_strict_subsets()
        self.assertFalse(set1.isdisjoint(set2))
        self.assertFalse(set2.isdisjoint(set1))

    def test_disjoint_equal(self):
        set1, set2 = self._make_equal_sets()
        self.assertFalse(set1.isdisjoint(set2))
        self.assertFalse(set2.isdisjoint(set1))

    def test_is_disjoint_non_Set(self):
        self.assertRaises(TypeError, self.test_set.isdisjoint, "a")

    #-------------------------------------------------
    # Tests for the issubset method. 
    #-------------------------------------------------

    def test_is_subset_empty(self):
        self.assertTrue(Set().issubset(Set()))

    def test_is_subset_non_empty(self):
        nonEmpty = Set([1, 2, 3])
        self.assertTrue(self.test_set.issubset(nonEmpty))

    def test_is_subset_subset(self):
        set1, set2 = self._make_strict_subsets()
        self.assertTrue(set1.issubset(set2))

    def test_is_subset_superset(self):
        set1, set2 = self._make_strict_subsets()
        self.assertFalse(set2.issubset(set1))

    def test_is_subset_equal(self):
        set1, set2 = self._make_equal_sets()
        self.assertTrue(set2.issubset(set1))

    def test_is_subset_intersecting(self):
        set1, set2 = self._make_intersecting_sets()
        self.assertFalse(set1.issubset(set2))
        self.assertFalse(set2.issubset(set1))

    def test_is_subset_disjoint(self):
        set1, set2 = self._make_disjoint_sets()
        self.assertFalse(set1.issubset(set2))
        self.assertFalse(set2.issubset(set1))

    def test_is_subset_non_Set(self):
        self.assertRaises(TypeError, self.test_set.issubset, "a")
                       
    #-------------------------------------------------
    # Tests for the issubset operator. 
    #-------------------------------------------------

    def test_is_subset_op_empty(self):
        self.assertTrue(Set() <= Set())

    def test_is_subset_op_non_Empty(self):
        nonEmpty = Set([1, 2, 3])
        self.assertTrue(self.test_set <= nonEmpty)

    def test_is_subset_op_subset(self):
        set1, set2 = self._make_strict_subsets()
        self.assertTrue(set1 <= set2)

    def test_is_subset_op_superset(self):
        set1, set2 = self._make_strict_subsets()
        self.assertFalse(set2 <= set1)

    def test_is_subset_op_equal(self):
        set1, set2 = self._make_equal_sets()
        self.assertTrue(set2 <= set1)

    def test_is_subset_op_intersecting(self):
        set1, set2 = self._make_intersecting_sets()
        self.assertFalse(set1 <= set2)
        self.assertFalse(set2 <= set1)

    def test_is_subset_op_disjoint(self):
        set1, set2 = self._make_disjoint_sets()
        self.assertFalse(set1 <= set2)
        self.assertFalse(set2 <= set1)

    def test_is_subset_op_non_Set(self):
        self.assertRaises(TypeError, self.test_set.__le__, "a")
                       

    #-------------------------------------------------
    # Tests for the proper subset operator. 
    #-------------------------------------------------
    def test_is_proper_subset_op_Empty(self):
        self.assertFalse(Set() < Set())

    def test_is_proper_subset_op_non_Empty(self):
        nonEmpty = Set([1, 2, 3])
        self.assertTrue(self.test_set < nonEmpty)

    def test_is_proper_subset_op_subset(self):
        set1, set2 = self._make_strict_subsets()
        self.assertTrue(set1 < set2)

    def test_is_proper_subset_op_superset(self):
        set1, set2 = self._make_strict_subsets()
        self.assertFalse(set2 < set1)

    def test_is_proper_subset_op_Equal(self):
        set1, set2 = self._make_equal_sets()
        self.assertFalse(set2 < set1)

    def test_is_proper_subset_op_intersecting(self):
        set1, set2 = self._make_intersecting_sets()
        self.assertFalse(set1 < set2)
        self.assertFalse(set2 < set1)

    def test_is_proper_subset_op_disjoint(self):
        set1, set2 = self._make_disjoint_sets()
        self.assertFalse(set1 < set2)
        self.assertFalse(set2 < set1)

    def test_is_proper_subset_op_non_Set(self):
        self.assertRaises(TypeError, self.test_set.__lt__, "a")

    #-------------------------------------------------
    # Tests for the issuperset method. 
    #-------------------------------------------------

    def test_is_superset_empty(self):
        self.assertTrue(Set().issubset(Set()))

    def test_is_superset_non_empty(self):
        nonEmpty = Set([1, 2, 3])
        self.assertTrue(nonEmpty.issuperset(self.test_set))

    def test_is_superset_super_Set(self):
        set1, set2 = self._make_strict_subsets()
        self.assertTrue(set2.issuperset(set1))

    def test_is_superset_subset(self):
        set1, set2 = self._make_strict_subsets()
        self.assertFalse(set1.issuperset(set2))

    def test_is_superset_equal(self):
        set1, set2 = self._make_equal_sets()
        self.assertTrue(set2.issuperset(set1))

    def test_is_superset_intersecting(self):
        set1, set2 = self._make_intersecting_sets()
        self.assertFalse(set1.issuperset(set2))
        self.assertFalse(set2.issuperset(set1))

    def test_is_superset_disjoint(self):
        set1, set2 = self._make_disjoint_sets()
        self.assertFalse(set1.issuperset(set2))
        self.assertFalse(set2.issuperset(set1))

    def test_is_superset_non_Set(self):
        self.assertRaises(TypeError, self.test_set.issuperset, "a")
                       
    #-------------------------------------------------
    # Tests for the issuperset operator. 
    #-------------------------------------------------

    def test_is_superset_op_empty(self):
        self.assertTrue(Set() >= Set())

    def test_is_superset_op_non_Empty(self):
        nonEmpty = Set([1, 2, 3])
        self.assertTrue(nonEmpty >= self.test_set)

    def test_is_superset_op_superset(self):
        set1, set2 = self._make_strict_subsets()
        self.assertTrue(set2 >= set1)

    def test_is_superset_op_subset(self):
        set1, set2 = self._make_strict_subsets()
        self.assertFalse(set1 >= set2)

    def test_is_superset_op_equal(self):
        set1, set2 = self._make_equal_sets()
        self.assertTrue(set2 >= set1)

    def test_is_superset_op_intersecting(self):
        set1, set2 = self._make_intersecting_sets()
        self.assertFalse(set1 >= set2)
        self.assertFalse(set2 >= set1)

    def test_is_superset_op_disjoint(self):
        set1, set2 = self._make_disjoint_sets()
        self.assertFalse(set1 >= set2)
        self.assertFalse(set2 >= set1)

    def test_is_superset_op_non_Set(self):
        self.assertRaises(TypeError, self.test_set.__ge__, "a")


    #-------------------------------------------------
    # Tests for the is proper superset operator. 
    #-------------------------------------------------
 
    def test_is_proper_superset_op_Empty(self):
        self.assertFalse(Set() > Set())

    def test_is_proper_superset_op_non_Empty(self):
        nonEmpty = Set([1, 2, 3])
        self.assertTrue(nonEmpty > self.test_set)

    def test_is_proper_superset_op_superset(self):
        set1, set2 = self._make_strict_subsets()
        self.assertTrue(set2 > set1)

    def test_is_proper_superset_op_subset(self):
        set1, set2 = self._make_strict_subsets()
        self.assertFalse(set1 > set2)

    def test_is_proper_superset_op_Equal(self):
        set1, set2 = self._make_equal_sets()
        self.assertFalse(set2 > set1)

    def test_is_proper_superset_op_intersecting(self):
        set1, set2 = self._make_intersecting_sets()
        self.assertFalse(set1 > set2)
        self.assertFalse(set2 > set1)

    def test_is_proper_superset_op_disjoint(self):
        set1, set2 = self._make_disjoint_sets()
        self.assertFalse(set1 > set2)
        self.assertFalse(set2 > set1)

    def test_is_proper_superset_op_non_Set(self):
        self.assertRaises(TypeError, self.test_set.__gt__, "a")       

    #-------------------------------------------------
    # Tests for union. 
    #------------------------------------------------- 
    
    def test_union_empty_empty(self):
        union = Set().union(Set())
        self.assertEqual(union, Set())

    def test_union_non_empty_empty(self):
        set1 = Set([1, 2, 3])
        equalSet1 = Set([1, 2, 3])
        union = set1.union(Set())
        self.assertEqual(union, equalSet1)

    def test_union_empty_non_empty(self):
        set1 = Set([1, 2, 3])
        equalSet1 = Set([1, 2, 3])
        union = Set().union(set1)
        self.assertEqual(union, equalSet1)

    def test_union_equal(self):
        set1, set2 = self._make_equal_sets()
        union = set1.union(set2)
        self.assertEqual(union, set1)
        self.assertEqual(union, set2)

    def test_union_subset(self):
        set1, set2 = self._make_strict_subsets()
        correct_union = Set(set(set1).union(set(set2)))
        union = set1.union(set2)
        self.assertEqual(union, correct_union)

    def test_union_superset(self):
        set1, set2 = self._make_strict_subsets()
        correct_union = Set(set(set2).union(set(set1)))
        union = set2.union(set1)
        self.assertEqual(union, correct_union)

    def test_union_disjoint(self):
        set1, set2 = self._make_disjoint_sets()
        correct_union = Set(set(set2).union(set(set1)))
        union = set2.union(set1)
        self.assertEqual(union, correct_union)

    def test_union_intersecting(self):
        set1, set2 = self._make_intersecting_sets()
        correct_union = Set(set(set2).union(set(set1)))
        union = set2.union(set1)
        self.assertEqual(union, correct_union)

    def test_union_non_Set(self):
        self.assertRaises(TypeError, self.test_set.union, "a")       

    #-------------------------------------------------
    # Tests for union operator. 
    #------------------------------------------------- 
    
    def test_union_op_empty_empty(self):
        union = Set() | Set()
        self.assertEqual(union, Set())

    def test_union_op_non_empty_Empty(self):
        set1 = Set([1, 2, 3])
        equalSet1 = Set([1, 2, 3])
        union = set1 | Set()
        self.assertEqual(union, equalSet1)

    def test_union_op_empty_non_Empty(self):
        set1 = Set([1, 2, 3])
        equalSet1 = Set([1, 2, 3])
        union = Set() | set1
        self.assertEqual(union, equalSet1)

    def test_union_op_equal(self):
        set1, set2 = self._make_equal_sets()
        union = set1 | set2
        self.assertEqual(union, set1)
        self.assertEqual(union, set2)

    def test_union_op_subset(self):
        set1, set2 = self._make_strict_subsets()
        correct_union = Set(set(set1).union(set(set2)))
        union = set1 | set2
        self.assertEqual(union, correct_union)

    def test_union_op_superset(self):
        set1, set2 = self._make_strict_subsets()
        correct_union = Set(set(set2).union(set(set1)))
        union = set2 | set1
        self.assertEqual(union, correct_union)

    def test_union_op_disjoint(self):
        set1, set2 = self._make_disjoint_sets()
        correct_union = Set(set(set2).union(set(set1)))
        union = set2 | set1
        self.assertEqual(union, correct_union)

    def test_union_op_intersecting(self):
        set1, set2 = self._make_intersecting_sets()
        correct_union = Set(set(set2).union(set(set1)))
        union = set2 | set1
        self.assertEqual(union, correct_union)

    def test_union_op_non_Set(self):
        self.assertRaises(TypeError, self.test_set.__or__, "a")     

    #-------------------------------------------------
    # Tests for intersection. 
    #------------------------------------------------- 
    
    def test_intersection_empty_empty(self):
        intersection = Set().intersection(Set())
        self.assertEqual(intersection, Set())

    def test_intersection_non_empty_empty(self):
        set1 = Set([1, 2, 3])
        intersection = set1.intersection(Set())
        self.assertEqual(intersection, Set())

    def test_intersection_empty_non_empty(self):
        set1 = Set([1, 2, 3])
        intersection = Set().intersection(set1)
        self.assertEqual(intersection, Set())

    def test_intersection_equal(self):
        set1, set2 = self._make_equal_sets()
        intersection = set1.intersection(set2)
        self.assertEqual(intersection, set1)
        self.assertEqual(intersection, set2)

    def test_intersection_subset(self):
        set1, set2 = self._make_strict_subsets()
        correct_intersection = Set(set(set1).intersection(set(set2)))
        intersection = set1.intersection(set2)
        self.assertEqual(intersection, correct_intersection)

    def test_intersection_superset(self):
        set1, set2 = self._make_strict_subsets()
        correct_intersection = Set(set(set2).intersection(set(set1)))
        intersection = set2.intersection(set1)
        self.assertEqual(intersection, correct_intersection)

    def test_intersection_disjoint(self):
        set1, set2 = self._make_disjoint_sets()
        correct_intersection = Set(set(set2).intersection(set(set1)))
        intersection = set2.intersection(set1)
        self.assertEqual(intersection, correct_intersection)

    def test_intersection_intersecting(self):
        set1, set2 = self._make_intersecting_sets()
        correct_intersection = Set(set(set2).intersection(set(set1)))
        intersection = set2.intersection(set1)
        self.assertEqual(intersection, correct_intersection)

    def test_intersection_non_Set(self):
        self.assertRaises(TypeError, self.test_set.intersection, "a")       

    #-------------------------------------------------
    # Tests for intersection operator. 
    #------------------------------------------------- 
    
    def test_intersection_op_empty_empty(self):
        intersection = Set() & Set()
        self.assertEqual(intersection, Set())

    def test_intersection_op_non_empty_Empty(self):
        set1 = Set([1, 2, 3])
        intersection = set1 & Set()
        self.assertEqual(intersection, Set())

    def test_intersection_op_empty_non_Empty(self):
        set1 = Set([1, 2, 3])
        intersection = Set() & set1
        self.assertEqual(intersection, Set())

    def test_intersection_op_equal(self):
        set1, set2 = self._make_equal_sets()
        intersection = set1 & set2
        self.assertEqual(intersection, set1)
        self.assertEqual(intersection, set2)

    def test_intersection_op_subset(self):
        set1, set2 = self._make_strict_subsets()
        correct_intersection = Set(set(set1).intersection(set(set2)))
        intersection = set1 & set2
        self.assertEqual(intersection, correct_intersection)

    def test_intersection_op_superset(self):
        set1, set2 = self._make_strict_subsets()
        correct_intersection = Set(set(set2).intersection(set(set1)))
        intersection = set2 & set1
        self.assertEqual(intersection, correct_intersection)

    def test_intersection_op_disjoint(self):
        set1, set2 = self._make_disjoint_sets()
        correct_intersection = Set(set(set2).intersection(set(set1)))
        intersection = set2 & set1
        self.assertEqual(intersection, correct_intersection)

    def test_intersection_op_intersecting(self):
        set1, set2 = self._make_intersecting_sets()
        correct_intersection = Set(set(set2).intersection(set(set1)))
        intersection = set2 & set1
        self.assertEqual(intersection, correct_intersection)

    def test_intersection_op_non_Set(self):
        self.assertRaises(TypeError, self.test_set.__and__, "a")     


    #-------------------------------------------------
    # Tests for symmetric_difference. 
    #------------------------------------------------- 
    
    def test_symmetric_difference_empty_empty(self):
        result = Set().symmetric_difference(Set())
        self.assertEqual(result, Set())

    def test_symmetric_difference_non_empty_Empty(self):
        set1 = Set([1, 2, 3])
        equalSet1 = Set([1, 2, 3])
        result = set1.symmetric_difference(Set())
        self.assertEqual(result, equalSet1)

    def test_symmetric_difference_empty_non_Empty(self):
        set1 = Set([1, 2, 3])
        equalSet1 = Set([1, 2, 3])
        result = Set().symmetric_difference(set1)
        self.assertEqual(result, equalSet1)

    def test_symmetric_difference_equal(self):
        set1, set2 = self._make_equal_sets()
        result = set1.symmetric_difference(set2)
        self.assertEqual(result, Set())

    def test_symmetric_difference_subset(self):
        set1, set2 = self._make_strict_subsets()
        correct_result = \
            Set(set(set1).symmetric_difference(set(set2)))
        result = set1.symmetric_difference(set2)
        self.assertEqual(result, correct_result)

    def test_symmetric_difference_superset(self):
        set1, set2 = self._make_strict_subsets()
        correct_result = \
            Set(set(set2).symmetric_difference(set(set1)))
        result = set2.symmetric_difference(set1)
        self.assertEqual(result, correct_result)

    def test_symmetric_difference_disjoint(self):
        set1, set2 = self._make_disjoint_sets()
        correct_result = \
            Set(set(set2).symmetric_difference(set(set1)))
        result = set2.symmetric_difference(set1)
        self.assertEqual(result, correct_result)

    def test_symmetric_difference_intersecting(self):
        set1, set2 = self._make_intersecting_sets()
        correct_result = \
            Set(set(set2).symmetric_difference(set(set1)))
        result = set2.symmetric_difference(set1)
        self.assertEqual(result, correct_result)

    def test_symmetric_difference_non_Set(self):
        self.assertRaises(TypeError, self.test_set.symmetric_difference, "a") 


    #-------------------------------------------------
    # Tests for symmetric_difference operator. 
    #------------------------------------------------- 
    
    def test_symmetric_difference_op_empty_Empty(self):
        result = Set() ^ Set()
        self.assertEqual(result, Set())

    def test_symmetric_difference_op_non_empty_Empty(self):
        set1 = Set([1, 2, 3])
        equalSet1 = Set([1, 2, 3])
        result = set1 ^ Set()
        self.assertEqual(result, equalSet1)

    def test_symmetric_difference_op_empty_non_Empty(self):
        set1 = Set([1, 2, 3])
        equalSet1 = Set([1, 2, 3])
        result = Set() ^ set1
        self.assertEqual(result, equalSet1)

    def test_symmetric_difference_op_equal(self):
        set1, set2 = self._make_equal_sets()
        result = set1 ^ set2
        self.assertEqual(result, Set())

    def test_symmetric_difference_op_subset(self):
        set1, set2 = self._make_strict_subsets()
        correct_result = \
            Set(set(set1).symmetric_difference(set(set2)))
        result = set1 ^ set2
        self.assertEqual(result, correct_result)

    def test_symmetric_difference_op_superset(self):
        set1, set2 = self._make_strict_subsets()
        correct_result = \
            Set(set(set2).symmetric_difference(set(set1)))
        result = set2 ^ set1
        self.assertEqual(result, correct_result)

    def test_symmetric_difference_op_disjoint(self):
        set1, set2 = self._make_disjoint_sets()
        correct_result = \
            Set(set(set2).symmetric_difference(set(set1)))
        result = set2 ^ set1
        self.assertEqual(result, correct_result)

    def test_symmetric_difference_op_intersecting(self):
        set1, set2 = self._make_intersecting_sets()
        correct_result = \
            Set(set(set2).symmetric_difference(set(set1)))
        result = set2 ^ set1
        self.assertEqual(result, correct_result)

    def test_symmetric_difference_op_non_Set(self):
        self.assertRaises(TypeError, self.test_set.__xor__, "a")   

    #-------------------------------------------------
    # Tests for copy. 
    #------------------------------------------------- 

    def test_copy_empty(self):
        set1 = Set()
        set1_copy = set1.copy()
        self.assertEqual(set1, set1_copy)

    def test_copy_non_empty(self):
        set1 = Set([1, 2, 3, "a", "b", "c"])
        set1_copy = set1.copy()
        self.assertEqual(set1, set1_copy)

    def test_copy_not_alias(self):
        set1 = Set([1, 2, 3, "a", "b", "c"])
        set1_copy = set1.copy()
        self.assertIsNot(set1, set1_copy)

    def test_copy_no_array_alias(self):
        set1 = Set([1, 2, 3, "a", "b", "c"])
        set1_copy = set1.copy()
        set1.pop()
        self.assertNotEqual(set1, set1_copy)

    def test_copy_is_shallow(self):
        the_list = [1, 2, 3]
        set1 = Set([the_list])
        set1_copy = set1.copy()
        the_list[0] = -1
        same_list = set1_copy.pop()
        self.assertEqual(the_list[0], same_list[0])

    #-------------------------------------------------
    # Tests for str and repr.
    #------------------------------------------------- 

    def test_str_empty(self):
        self.assertEqual(str(Set()), 'set([])')
        self.assertEqual(repr(Set()), 'set([])')

    def test_str_non_empty(self):
        # This test takes advantage of the fact that our string
        # representation is exactly the same as the python set. 
        set1 = Set(["a", "b", "c", 1, 2, 3])
        
        py_set1 = set(["a", "b", "c", 1, 2, 3])
        py_set2 = eval(str(set1))
        
        self.assertEqual(py_set1, py_set2)
        
        py_set2 = eval(repr(set1))
        
        self.assertEqual(py_set1, py_set2)

    #-------------------------------------------------
    # Iterator tests. 
    #------------------------------------------------- 

    def test_iterator_empty(self):
        for _ in self.test_set:
            #Should never get here.  Raise an exception if we do.
            self.assertTrue(False)

    def test_iterator_non_empty(self):
        set1 = Set([1, 2, 3, "a", "b", "c"])
        py_set1 = set([1, 2, 3, "a", "b", "c"])
        visited = []

        for item in set1:
            visited.append(item)

        self.assertEqual(py_set1, set(visited))
        self.assertEqual(len(py_set1), len(visited))
        

    def test_iterator_directly(self):
        set1 = Set([1, 2, 3, "a", "b", "c"])
        py_set1 = set([1, 2, 3, "a", "b", "c"])
        visited = []
        it = iter(set1)
        
        for item in it:
            visited.append(item)

        self.assertEqual(py_set1, set(visited))
        self.assertEqual(len(py_set1), len(visited))


    #-------------------------------------------------
    # Tests for the discard method. 
    #-------------------------------------------------
    def test_discard_items_not_in_set(self):
        
        test = Set([1, 2, 3, "a", "b", "c"])
        testOther = Set([1, 2, 3, "a", "b", "c"])
        
        test.discard("d")
        test.discard(0)
        test.discard("e")
        
        self.assertEqual(test, testOther)
        
    def test_discard_items_in_set(self):
        
        test = Set([1, 2, 3, "a", "b", "c"])
        testOther = Set([ 3, "a", "c"])
        
        test.discard(1)
        test.discard(2)
        test.discard("b")
        
        self.assertEqual(test, testOther)    
        
    def test_discard_items_at_back(self):
            
        test = Set([1, 2, 3, "a", "b", "c"])
        testOther = Set([1, 2, 3])
        
        test.discard("c")
        test.discard("b")
        test.discard("a")
        
        self.assertEqual(test, testOther)
    #-------------------------------------------------
    # Tests for the remove method. 
    #-------------------------------------------------
    
    def test_remove_items_not_in_set(self):
        
        test = Set([1, 2, 3, "a", "b", "c"])
        
        self.assertRaises(KeyError, test.remove, "d")  
        self.assertRaises(KeyError, test.remove, 5) 
        
    def test_remove_items_in_set(self):
        
        test = Set([1, 2, 3, "a", "b", "c"])
        testOther = Set([ 3, "a", "c"])
        
        test.remove(1)
        test.remove(2)
        test.remove("b")
        
        self.assertEqual(test, testOther)
        
    def test_remove_items_in_set_already_removed(self):
        
        test = Set([1, 2, 3, "a", "b", "c"])
        
        test.remove(1)
        test.remove(2)
        test.remove("c")
        
        self.assertRaises(KeyError, test.remove, "c")
        
    def test_remove_empty_set(self):
        
        test = Set()
        
        self.assertRaises(KeyError, test.remove, 1)
        
        
    
    #-------------------------------------------------
    # Tests for the pop method. 
    #-------------------------------------------------
    
    def test_pop(self):
        
        test = Set([1, 2, 3, "a", "b", "c"])
        testOther = Set([1, 2, 3, "a", "b", "c"])
        
        testOther.remove(test.pop())
        
        self.assertEqual(test, testOther)
        
    def test_pop_not_equal(self):
        
        test = Set([1, 2, 3, "a", "b", "c"])
        testOther = Set([1, 2, 3, "a", "b", "c"])
        
        test.pop()
        
        self.assertNotEqual(test, testOther)
        
    def test_pop_element(self):
        
        test = Set([1, 2, 3, "a", "b", "c"])
        
        elem = test.pop()
        
        self.assertRaises(KeyError, test.remove, elem)
        
    def test_pop_empty_set(self):
        
        test = Set()
        
        self.assertRaises(KeyError, test.pop)
        
        

if __name__ == "__main__":
    unittest.main()
