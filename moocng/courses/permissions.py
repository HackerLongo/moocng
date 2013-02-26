# -*- coding: utf-8 -*-

# Copyright 2012 Rooter Analysis S.L.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def moocng_has_perm(user, permission_code, obj):
    if permission_code.startswith('courses'):
        return check_mooc_courses_permission(user, permission_code, obj)
    if permission_code.startswith('units'):
        return check_mooc_units_permission(user, permission_code, obj)
    return False


def check_mooc_courses_permission(user, permission_code, course):
    # TODO. Reviewer. Mod slug perm
    if permission_code in  ['courses.list_course', 'courses.get_course']:
        return True
    elif permission_code == 'courses.add_course':
        if user.is_staff:
            return True
        else:
            return False
    elif permission_code == 'courses.change_course':
        if user.is_staff or is_course_teacher(user, course) or is_course_owner(user, course):
            return True
        else:
            return False
    elif permission_code == 'courses.delete_course':
        if user.is_staff or is_course_owner(user, course):
            return True
        else:
            return False
    return False


def check_mooc_units_permission(user, permission_code, obj):
    pass


# Exists is_teacher in moocng.courses.utils, but check all courses
def is_course_teacher(user, course):
    if course:
        return course.teachers.filter(id=user.id).exists()
    else:
        return False


def is_course_owner(user, course):
    if course:
        return course.owner == user
    else:
        return False
