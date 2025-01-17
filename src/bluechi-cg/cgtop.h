#pragma once

#include <stdbool.h>

#include "hashmap.h"

#include "common.h"


typedef struct CGTopAgent {
        int ref_count;

        bool systemd_user;
        char *api_bus_service_name;
        long interval_msec;
        char *root;


        sd_bus *api_bus;
        sd_bus *systemd_dbus;
        sd_bus_slot *cgtop_slot;
        sd_event *event;

        Hashmap *cg_a;
        Hashmap *cg_b;
        unsigned iteration;
} CGTopAgent;

CGTopAgent *cgtop_agent_new(const char *root);
CGTopAgent *cgtop_agent_ref(CGTopAgent *agent);
void cgtop_agent_unref(CGTopAgent *agent);

int cgtop_agent_setup_timer(CGTopAgent *agent);

DEFINE_CLEANUP_FUNC(CGTopAgent, cgtop_agent_unref)
#define _cleanup_cgtop_agent_ _cleanup_(cgtop_agent_unrefp)
