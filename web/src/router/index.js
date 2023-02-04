import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/dashboard/HomeView.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            // 非懒加载
            component: LoginView
        },
        {
            path: "/login",
            name: "login",
            component: LoginView
        },
        {
            path: '/dashboard',
            component: () => import('../views/DashboardView.vue'),
            children: [
                {
                    path: '',
                    name: 'home',
                    component: () => import('../views/dashboard/HomeView.vue')
                },
                {
                    path: 'overview',
                    children: [
                        {
                            path: 'permission',
                            name: 'overview-permission',
                            // () => import 懒加载
                            component: () => import('../views/dashboard/overview/PermissionOverviewView.vue')
                        },
                        {
                            path: 'machine',
                            name: 'overview-machine',
                            component: () => import('../views/dashboard/overview/MachineOverviewView.vue')
                        },
                        {
                            path: 'concept',
                            name: 'overview-concept',
                            component: () => import('../views/dashboard/overview/ConceptOverviewView.vue')
                        },
                        {
                            path: 'repo-config',
                            name: 'overview-repo-config',
                            component: () => import('../views/dashboard/overview/RepoConfigOverviewView.vue')
                        }
                    ]
                },
                {
                    path: 'permission-control',
                    children: [
                        {
                            path: 'group-mgmt',
                            name: 'permission-control-group-mgmt',
                            component: () => import('../views/dashboard/permission-control/GroupMgmtView.vue')
                        },
                        {
                            path: 'member-mgmt',
                            name: 'permission-control-member-mgmt',
                            component: () => import('../views/dashboard/permission-control/MemberMgmtView.vue')
                        }
                    ]
                },
                {
                    path: 'biz-concept',
                    children: [
                        {
                            path: 'machine',
                            name: 'biz-concept-machine',
                            component: () => import("../views/dashboard/biz-concept/MachineView.vue")
                        },
                        {
                            path: 'group',
                            name: 'biz-concept-group',
                            component: () => import("../views/dashboard/biz-concept/GroupView.vue")
                        },
                        {
                            path: 'safe-group',
                            name: 'biz-concept-safe-group',
                            component: () => import('../views/dashboard/biz-concept/SafeGroupView.vue')
                        },
                        {
                            path: 'res-pool',
                            name: 'biz-concept-res-pool',
                            component: () => import('../views/dashboard/biz-concept/ResPoolView.vue')
                        }
                    ]
                },
                {
                    path: 'config',
                    children: [
                        {
                            path: 'repo',
                            name: 'config-repo',
                            component: () => import('../views/dashboard/config/RepoView.vue')
                        },
                        {
                            path: 'vcs',
                            name: 'config-vcs',
                            component: () => import('../views/dashboard/config/VCSView.vue'),
                            children: [
                                {
                                    path: '',
                                    component: () => import("../views/dashboard/config/vcs/RepoStepView.vue")
                                },
                                {
                                    path: "repo-step",
                                    name: "repo-step",
                                    component: () => import("../views/dashboard/config/vcs/RepoStepView.vue")
                                },
                                {
                                    path: "directory-step",
                                    name: "directory-step",
                                    component: () => import("../views/dashboard/config/vcs/DirectoryStepView.vue")
                                },
                                {
                                    path: "target-step",
                                    name: "target-step",
                                    component: () => import("../views/dashboard/config/vcs/TargetStepView.vue")
                                },
                                {
                                    path: "execute-step",
                                    name: "execute-step",
                                    component: () => import("../views/dashboard/config/vcs/ExecuteStepView.vue")
                                },
                                {
                                    path: "finsh-step",
                                    name: "finsh-step",
                                    component: () => import("../views/dashboard/config/vcs/FinshStepVIew.vue")
                                }
                            ]
                        }
                    ]
                },
                {
                    path: 'audit',
                    name: 'audit',
                    component: () => import('../views/dashboard/AuditView.vue')
                },
                {
                    path: 'about-me',
                    name: 'about-me',
                    // route level code-splitting
                    // this generates a separate chunk (About.[hash].js) for this route
                    // which is lazy-loaded when the route is visited.
                    component: () => import('../views/dashboard/AboutMeView.vue')
                }
            ]
        },
        {
            path: '/about',
            name: 'about',
            component: () => import('../views/AboutView.vue')
        }
    ]
})

export default router
