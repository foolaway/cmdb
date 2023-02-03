import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/overview',
      children: [
        {
          path: 'permission',
          name: 'overview-permission',
          component: () => import('../views/overview/PermissionOverviewView.vue')
        },
        {
          path: 'machine',
          name: 'overview-machine',
          component: () => import('../views/overview/MachineOverviewView.vue')
        },
        {
          path: 'concept',
          name: 'overview-concept',
          component: () => import('../views/overview/ConceptOverviewView.vue')
        },
        {
          path: 'repo-config',
          name: 'overview-repo-config',
          component: () => import('../views/overview/RepoConfigOverviewView.vue')
        }
      ]
    },
    {
      path: '/permission-control',
      children: [
        {
          path: 'group-mgmt',
          name: 'permission-control-group-mgmt',
          component: () => import('../views/permission-control/GroupMgmtView.vue')
        },
        {
          path: 'member-mgmt',
          name: 'permission-control-member-mgmt',
          component: () => import('../views/permission-control/MemberMgmtView.vue')
        }
      ]
    },
    {
      path: '/biz-concept',
      children: [
        {
          path: 'machine',
          name: 'biz-concept-machine',
          component: () => import("../views/biz-concept/MachineView.vue")
        },
        {
          path: 'group',
          name: 'biz-concept-group',
          component: () => import("../views/biz-concept/GroupView.vue")
        },
        {
          path: 'safe-group',
          name: 'biz-concept-safe-group',
          component: () => import('../views/biz-concept/SafeGroupView.vue')
        },
        {
          path: 'res-pool',
          name: 'biz-concept-res-pool',
          component: () => import('../views/biz-concept/ResPoolView.vue')
        }
      ]
    },
    {
      path: '/config',
      children: [
        {
          path: 'repo',
          name: 'config-repo',
          component: () => import('../views/config/RepoView.vue')
        },
        {
          path: 'vcs',
          name: 'config-vcs',
          component: () => import('../views/config/VCSView.vue')
        }
      ]
    },
    {
      path: '/audit',
      name: 'audit',
      component: () => import('../views/AuditView.vue')
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
