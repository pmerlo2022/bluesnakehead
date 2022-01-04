# AMS

# Table of Contents
<!-- toc -->

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

<!-- toc -->
# Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision |
| --- | ---- | ---- | ------------- | -------- | -------------------------- |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1A | 10.6.2.1/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1B | 10.6.2.2/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF2A | 10.6.2.3/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF2B | 10.6.2.4/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF3A | 10.6.2.5/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF3B | 10.6.2.6/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF4A | 10.6.2.7/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF4B | 10.6.2.8/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF5A | 10.6.2.9/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF5B | 10.6.2.10/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF6A | 10.6.2.11/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF6B | 10.6.2.12/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF7A | 10.6.2.13/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF7B | 10.6.2.14/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF8A | 10.6.2.15/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF8B | 10.6.2.16/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF9A | 10.6.2.17/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF9B | 10.6.2.18/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF10A | 10.6.2.19/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF10B | 10.6.2.20/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF11A | 10.6.2.21/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF11B | 10.6.2.22/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF12A | 10.6.2.23/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF12B | 10.6.2.24/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF13A | 10.6.2.25/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF13B | 10.6.2.26/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF14A | 10.6.2.27/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF14B | 10.6.2.28/24 | 7280R | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE1 | 10.6.1.1/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE2 | 10.6.1.2/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE3 | 10.6.1.3/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE4 | 10.6.1.4/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF1A | 10.6.34.1/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF1B | 10.6.34.2/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF2A | 10.6.34.3/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF2B | 10.6.34.4/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF3A | 10.6.34.5/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF3B | 10.6.34.6/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF4A | 10.6.34.7/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF4B | 10.6.34.8/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF5A | 10.6.34.9/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF5B | 10.6.34.10/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF6A | 10.6.34.11/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF6B | 10.6.34.12/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF7A | 10.6.34.13/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF7B | 10.6.34.14/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF8A | 10.6.34.15/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF8B | 10.6.34.16/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF9A | 10.6.34.17/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF9B | 10.6.34.18/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF10A | 10.6.34.19/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF10B | 10.6.34.20/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF11A | 10.6.34.21/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF11B | 10.6.34.22/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF12A | 10.6.34.23/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF12B | 10.6.34.24/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF13A | 10.6.34.25/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF13B | 10.6.34.26/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF14A | 10.6.34.27/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF14B | 10.6.34.28/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE1 | 10.6.33.1/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE2 | 10.6.33.2/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE3 | 10.6.33.3/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE4 | 10.6.33.4/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF1A | 10.6.32.1/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF1B | 10.6.32.2/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF2A | 10.6.32.3/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF2B | 10.6.32.4/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF3A | 10.6.32.5/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF3B | 10.6.32.6/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF4A | 10.6.32.7/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF4B | 10.6.32.8/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF5A | 10.6.32.9/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF5B | 10.6.32.10/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF6A | 10.6.32.11/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF6B | 10.6.32.12/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF7A | 10.6.32.13/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF7B | 10.6.32.14/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF8A | 10.6.32.15/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF8B | 10.6.32.16/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF9A | 10.6.32.17/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF9B | 10.6.32.18/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF10A | 10.6.32.19/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF10B | 10.6.32.20/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF11A | 10.6.32.21/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF11B | 10.6.32.22/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF12A | 10.6.32.23/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF12B | 10.6.32.24/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF13A | 10.6.32.25/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF13B | 10.6.32.26/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF14A | 10.6.32.27/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF14B | 10.6.32.28/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE1 | 10.6.65.1/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE2 | 10.6.65.2/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE3 | 10.6.65.3/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE4 | 10.6.65.4/24 | vEOS-LAB | Provisioned |
| AMS | super-spine | SUPER-SPINE1 | 10.6.0.1/24 | 7060 | Provisioned |
| AMS | super-spine | SUPER-SPINE2 | 10.6.0.2/24 | 7280R | Provisioned |
| AMS | super-spine | SUPER-SPINE3 | 10.6.0.3/24 | 7280R | Provisioned |
| AMS | super-spine | SUPER-SPINE4 | 10.6.0.4/24 | 7280R | Provisioned |
| AMS | super-spine | SUPER-SPINE5 | 10.6.0.5/24 | 7280R | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | DC1-POD1-LEAF1A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF1B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF1B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet28/1 | l3leaf | DC1-POD1-LEAF1B | Ethernet28/1 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet1/1 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet1/1 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet1/1 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet1/1 |
| l3leaf | DC1-POD1-LEAF1B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet2/1 |
| l3leaf | DC1-POD1-LEAF1B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet2/1 |
| l3leaf | DC1-POD1-LEAF1B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet2/1 |
| l3leaf | DC1-POD1-LEAF1B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet2/1 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF2B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF2B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet3/1 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet3/1 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet3/1 |
| l3leaf | DC1-POD1-LEAF2A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet3/1 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet4/1 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet4/1 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet4/1 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet4/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF3B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF3B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet5/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet5/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet5/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet5/1 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet6/1 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet6/1 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet6/1 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet6/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF4B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF4B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet7/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet7/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet7/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet7/1 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet8/1 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet8/1 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet8/1 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet8/1 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF5B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF5B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet9/1 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet9/1 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet9/1 |
| l3leaf | DC1-POD1-LEAF5A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet9/1 |
| l3leaf | DC1-POD1-LEAF5B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet10/1 |
| l3leaf | DC1-POD1-LEAF5B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet10/1 |
| l3leaf | DC1-POD1-LEAF5B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet10/1 |
| l3leaf | DC1-POD1-LEAF5B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet10/1 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF6B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF6B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet11/1 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet11/1 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet11/1 |
| l3leaf | DC1-POD1-LEAF6A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet11/1 |
| l3leaf | DC1-POD1-LEAF6B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet12/1 |
| l3leaf | DC1-POD1-LEAF6B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet12/1 |
| l3leaf | DC1-POD1-LEAF6B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet12/1 |
| l3leaf | DC1-POD1-LEAF6B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet12/1 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF7B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF7B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet13/1 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet13/1 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet13/1 |
| l3leaf | DC1-POD1-LEAF7A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet13/1 |
| l3leaf | DC1-POD1-LEAF7B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet14/1 |
| l3leaf | DC1-POD1-LEAF7B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet14/1 |
| l3leaf | DC1-POD1-LEAF7B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet14/1 |
| l3leaf | DC1-POD1-LEAF7B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet14/1 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF8B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF8B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF8A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF8B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF8B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF8B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF8B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF9B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF9B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet17/1 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet17/1 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet17/1 |
| l3leaf | DC1-POD1-LEAF9A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet17/1 |
| l3leaf | DC1-POD1-LEAF9B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet18/1 |
| l3leaf | DC1-POD1-LEAF9B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet18/1 |
| l3leaf | DC1-POD1-LEAF9B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet18/1 |
| l3leaf | DC1-POD1-LEAF9B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet18/1 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF10B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF10B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet19/1 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet19/1 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet19/1 |
| l3leaf | DC1-POD1-LEAF10A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet19/1 |
| l3leaf | DC1-POD1-LEAF10B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet20/1 |
| l3leaf | DC1-POD1-LEAF10B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet20/1 |
| l3leaf | DC1-POD1-LEAF10B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet20/1 |
| l3leaf | DC1-POD1-LEAF10B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet20/1 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF11B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF11B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet21/1 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet21/1 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet21/1 |
| l3leaf | DC1-POD1-LEAF11A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet21/1 |
| l3leaf | DC1-POD1-LEAF11B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet22/1 |
| l3leaf | DC1-POD1-LEAF11B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet22/1 |
| l3leaf | DC1-POD1-LEAF11B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet22/1 |
| l3leaf | DC1-POD1-LEAF11B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet22/1 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF12B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF12B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet23/1 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet23/1 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet23/1 |
| l3leaf | DC1-POD1-LEAF12A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet23/1 |
| l3leaf | DC1-POD1-LEAF12B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet24/1 |
| l3leaf | DC1-POD1-LEAF12B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet24/1 |
| l3leaf | DC1-POD1-LEAF12B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet24/1 |
| l3leaf | DC1-POD1-LEAF12B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet24/1 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF13B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF13B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet25/1 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet25/1 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet25/1 |
| l3leaf | DC1-POD1-LEAF13A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet25/1 |
| l3leaf | DC1-POD1-LEAF13B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet26/1 |
| l3leaf | DC1-POD1-LEAF13B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet26/1 |
| l3leaf | DC1-POD1-LEAF13B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet26/1 |
| l3leaf | DC1-POD1-LEAF13B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet26/1 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF14B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF14B | Ethernet16/1 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet27/1 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet27/1 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet27/1 |
| l3leaf | DC1-POD1-LEAF14A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet27/1 |
| l3leaf | DC1-POD1-LEAF14B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet28/1 |
| l3leaf | DC1-POD1-LEAF14B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet28/1 |
| l3leaf | DC1-POD1-LEAF14B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet28/1 |
| l3leaf | DC1-POD1-LEAF14B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet28/1 |
| spine | DC1-POD1-SPINE1 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet1/1 |
| spine | DC1-POD1-SPINE1 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet1/1 |
| spine | DC1-POD1-SPINE1 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet1/1 |
| spine | DC1-POD1-SPINE1 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet1/1 |
| spine | DC1-POD1-SPINE2 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet2/1 |
| spine | DC1-POD1-SPINE2 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet2/1 |
| spine | DC1-POD1-SPINE2 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet2/1 |
| spine | DC1-POD1-SPINE2 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet2/1 |
| spine | DC1-POD1-SPINE3 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet3/1 |
| spine | DC1-POD1-SPINE3 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet3/1 |
| spine | DC1-POD1-SPINE3 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet3/1 |
| spine | DC1-POD1-SPINE3 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet3/1 |
| spine | DC1-POD1-SPINE4 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet4/1 |
| spine | DC1-POD1-SPINE4 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet4/1 |
| spine | DC1-POD1-SPINE4 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet4/1 |
| spine | DC1-POD1-SPINE4 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet4/1 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF1B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF1B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet1/1 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet1/1 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet1/1 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet1/1 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet2/1 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet2/1 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet2/1 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet2/1 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF2B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF2B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet3/1 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet3/1 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet3/1 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet3/1 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4/1 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet4/1 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet4/1 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet4/1 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF3B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF3B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet5/1 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5/1 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet5/1 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet5/1 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet6/1 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet6/1 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet6/1 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet6/1 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF4B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF4B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet7/1 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet7/1 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet7/1 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7/1 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet8/1 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet8/1 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet8/1 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet8/1 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF5B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF5B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet9/1 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet9/1 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet9/1 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet9/1 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet10/1 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet10/1 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet10/1 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet10/1 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF6B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF6B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet11/1 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet11/1 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet11/1 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet11/1 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet12/1 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet12/1 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet12/1 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet12/1 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF7B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF7B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet13/1 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet13/1 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet13/1 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet13/1 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet14/1 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet14/1 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet14/1 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet14/1 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF8B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF8B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF9B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF9B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet17/1 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet17/1 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet17/1 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet17/1 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet18/1 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet18/1 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet18/1 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet18/1 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF10B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF10B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet19/1 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet19/1 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet19/1 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet19/1 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet20/1 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet20/1 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet20/1 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet20/1 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF11B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF11B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet21/1 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet21/1 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet21/1 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet21/1 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet22/1 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet22/1 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet22/1 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet22/1 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF12B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF12B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet23/1 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet23/1 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet23/1 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet23/1 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet24/1 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet24/1 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet24/1 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet24/1 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF13B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF13B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet25/1 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet25/1 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet25/1 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet25/1 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet26/1 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet26/1 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet26/1 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet26/1 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet15/1 | mlag_peer | DC1-POD2-LEAF14B | Ethernet15/1 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet16/1 | mlag_peer | DC1-POD2-LEAF14B | Ethernet16/1 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet27/1 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet27/1 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet27/1 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet27/1 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet28/1 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet28/1 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet28/1 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet28/1 |
| spine | DC1-POD2-SPINE1 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet5/1 |
| spine | DC1-POD2-SPINE1 | Ethernet29/2 | super-spine | SUPER-SPINE1 | Ethernet5/2 |
| spine | DC1-POD2-SPINE1 | Ethernet29/3 | super-spine | SUPER-SPINE2 | Ethernet5/3 |
| spine | DC1-POD2-SPINE1 | Ethernet29/4 | super-spine | SUPER-SPINE2 | Ethernet5/4 |
| spine | DC1-POD2-SPINE1 | Ethernet30/1 | super-spine | SUPER-SPINE3 | Ethernet6/1 |
| spine | DC1-POD2-SPINE1 | Ethernet30/2 | super-spine | SUPER-SPINE3 | Ethernet6/2 |
| spine | DC1-POD2-SPINE1 | Ethernet30/3 | super-spine | SUPER-SPINE4 | Ethernet6/3 |
| spine | DC1-POD2-SPINE1 | Ethernet30/4 | super-spine | SUPER-SPINE4 | Ethernet6/4 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF1B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF1B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet28/1 | l3leaf | DC2-POD1-LEAF1B | Ethernet28/1 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet1/1 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet1/1 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet1/1 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet1/1 |
| l3leaf | DC2-POD1-LEAF1B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet2/1 |
| l3leaf | DC2-POD1-LEAF1B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet2/1 |
| l3leaf | DC2-POD1-LEAF1B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet2/1 |
| l3leaf | DC2-POD1-LEAF1B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet2/1 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF2B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF2B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet3/1 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet3/1 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet3/1 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet3/1 |
| l3leaf | DC2-POD1-LEAF2B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet4/1 |
| l3leaf | DC2-POD1-LEAF2B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet4/1 |
| l3leaf | DC2-POD1-LEAF2B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet4/1 |
| l3leaf | DC2-POD1-LEAF2B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet4/1 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF3B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF3B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet5/1 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet5/1 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet5/1 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet5/1 |
| l3leaf | DC2-POD1-LEAF3B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet6/1 |
| l3leaf | DC2-POD1-LEAF3B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet6/1 |
| l3leaf | DC2-POD1-LEAF3B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet6/1 |
| l3leaf | DC2-POD1-LEAF3B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet6/1 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF4B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF4B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet7/1 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet7/1 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet7/1 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet7/1 |
| l3leaf | DC2-POD1-LEAF4B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet8/1 |
| l3leaf | DC2-POD1-LEAF4B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet8/1 |
| l3leaf | DC2-POD1-LEAF4B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet8/1 |
| l3leaf | DC2-POD1-LEAF4B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet8/1 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF5B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF5B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet9/1 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet9/1 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet9/1 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet9/1 |
| l3leaf | DC2-POD1-LEAF5B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet10/1 |
| l3leaf | DC2-POD1-LEAF5B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet10/1 |
| l3leaf | DC2-POD1-LEAF5B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet10/1 |
| l3leaf | DC2-POD1-LEAF5B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet10/1 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF6B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF6B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet11/1 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet11/1 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet11/1 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet11/1 |
| l3leaf | DC2-POD1-LEAF6B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet12/1 |
| l3leaf | DC2-POD1-LEAF6B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet12/1 |
| l3leaf | DC2-POD1-LEAF6B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet12/1 |
| l3leaf | DC2-POD1-LEAF6B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet12/1 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF7B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF7B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet13/1 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet13/1 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet13/1 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet13/1 |
| l3leaf | DC2-POD1-LEAF7B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet14/1 |
| l3leaf | DC2-POD1-LEAF7B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet14/1 |
| l3leaf | DC2-POD1-LEAF7B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet14/1 |
| l3leaf | DC2-POD1-LEAF7B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet14/1 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF8B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF8B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF8B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF8B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF8B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF8B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF9B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF9B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet17/1 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet17/1 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet17/1 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet17/1 |
| l3leaf | DC2-POD1-LEAF9B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet18/1 |
| l3leaf | DC2-POD1-LEAF9B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet18/1 |
| l3leaf | DC2-POD1-LEAF9B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet18/1 |
| l3leaf | DC2-POD1-LEAF9B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet18/1 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF10B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF10B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet19/1 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet19/1 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet19/1 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet19/1 |
| l3leaf | DC2-POD1-LEAF10B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet20/1 |
| l3leaf | DC2-POD1-LEAF10B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet20/1 |
| l3leaf | DC2-POD1-LEAF10B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet20/1 |
| l3leaf | DC2-POD1-LEAF10B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet20/1 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF11B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF11B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet21/1 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet21/1 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet21/1 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet21/1 |
| l3leaf | DC2-POD1-LEAF11B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet22/1 |
| l3leaf | DC2-POD1-LEAF11B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet22/1 |
| l3leaf | DC2-POD1-LEAF11B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet22/1 |
| l3leaf | DC2-POD1-LEAF11B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet22/1 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF12B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF12B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet23/1 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet23/1 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet23/1 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet23/1 |
| l3leaf | DC2-POD1-LEAF12B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet24/1 |
| l3leaf | DC2-POD1-LEAF12B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet24/1 |
| l3leaf | DC2-POD1-LEAF12B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet24/1 |
| l3leaf | DC2-POD1-LEAF12B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet24/1 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF13B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF13B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet25/1 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet25/1 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet25/1 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet25/1 |
| l3leaf | DC2-POD1-LEAF13B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet26/1 |
| l3leaf | DC2-POD1-LEAF13B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet26/1 |
| l3leaf | DC2-POD1-LEAF13B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet26/1 |
| l3leaf | DC2-POD1-LEAF13B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet26/1 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF14B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF14B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet27/1 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet27/1 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet27/1 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet27/1 |
| l3leaf | DC2-POD1-LEAF14B | Ethernet29/1 | spine | DC2-POD1-SPINE1 | Ethernet28/1 |
| l3leaf | DC2-POD1-LEAF14B | Ethernet30/1 | spine | DC2-POD1-SPINE2 | Ethernet28/1 |
| l3leaf | DC2-POD1-LEAF14B | Ethernet31/1 | spine | DC2-POD1-SPINE3 | Ethernet28/1 |
| l3leaf | DC2-POD1-LEAF14B | Ethernet32/1 | spine | DC2-POD1-SPINE4 | Ethernet28/1 |
| spine | DC2-POD1-SPINE1 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet9/1 |
| spine | DC2-POD1-SPINE1 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet9/1 |
| spine | DC2-POD1-SPINE1 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet9/1 |
| spine | DC2-POD1-SPINE1 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet9/1 |
| spine | DC2-POD1-SPINE2 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet10/1 |
| spine | DC2-POD1-SPINE2 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet10/1 |
| spine | DC2-POD1-SPINE2 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet10/1 |
| spine | DC2-POD1-SPINE2 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet10/1 |
| spine | DC2-POD1-SPINE3 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet11/1 |
| spine | DC2-POD1-SPINE3 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet11/1 |
| spine | DC2-POD1-SPINE3 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet11/1 |
| spine | DC2-POD1-SPINE3 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet11/1 |
| spine | DC2-POD1-SPINE4 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet12/1 |
| spine | DC2-POD1-SPINE4 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet12/1 |
| spine | DC2-POD1-SPINE4 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet12/1 |
| spine | DC2-POD1-SPINE4 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet12/1 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.16.1.0/24 | 256 | 32 | 12.5 % |
| 172.16.2.0/24 | 256 | 16 | 6.25 % |
| 172.16.32.0/24 | 256 | 32 | 12.5 % |
| 172.17.1.0/24 | 256 | 224 | 87.5 % |
| 172.17.2.0/24 | 256 | 140 | 54.69 % |
| 172.17.32.0/24 | 256 | 224 | 87.5 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| DC1-POD1-LEAF1A | Ethernet28/1 | 200.200.200.104/24 | DC1-POD1-LEAF1B | Ethernet28/1 | 200.200.200.204/24 |
| DC1-POD1-LEAF1A | Ethernet29/1 | 172.17.1.33/31 | DC1-POD1-SPINE1 | Ethernet1/1 | 172.17.1.32/31 |
| DC1-POD1-LEAF1A | Ethernet30/1 | 172.17.1.35/31 | DC1-POD1-SPINE2 | Ethernet1/1 | 172.17.1.34/31 |
| DC1-POD1-LEAF1A | Ethernet31/1 | 172.17.1.37/31 | DC1-POD1-SPINE3 | Ethernet1/1 | 172.17.1.36/31 |
| DC1-POD1-LEAF1A | Ethernet32/1 | 172.17.1.39/31 | DC1-POD1-SPINE4 | Ethernet1/1 | 172.17.1.38/31 |
| DC1-POD1-LEAF1B | Ethernet29/1 | 172.17.1.41/31 | DC1-POD1-SPINE1 | Ethernet2/1 | 172.17.1.40/31 |
| DC1-POD1-LEAF1B | Ethernet30/1 | 172.17.1.43/31 | DC1-POD1-SPINE2 | Ethernet2/1 | 172.17.1.42/31 |
| DC1-POD1-LEAF1B | Ethernet31/1 | 172.17.1.45/31 | DC1-POD1-SPINE3 | Ethernet2/1 | 172.17.1.44/31 |
| DC1-POD1-LEAF1B | Ethernet32/1 | 172.17.1.47/31 | DC1-POD1-SPINE4 | Ethernet2/1 | 172.17.1.46/31 |
| DC1-POD1-LEAF2A | Ethernet29/1 | 172.17.1.49/31 | DC1-POD1-SPINE1 | Ethernet3/1 | 172.17.1.48/31 |
| DC1-POD1-LEAF2A | Ethernet30/1 | 172.17.1.51/31 | DC1-POD1-SPINE2 | Ethernet3/1 | 172.17.1.50/31 |
| DC1-POD1-LEAF2A | Ethernet31/1 | 172.17.1.53/31 | DC1-POD1-SPINE3 | Ethernet3/1 | 172.17.1.52/31 |
| DC1-POD1-LEAF2A | Ethernet32/1 | 172.17.1.55/31 | DC1-POD1-SPINE4 | Ethernet3/1 | 172.17.1.54/31 |
| DC1-POD1-LEAF2B | Ethernet29/1 | 172.17.1.57/31 | DC1-POD1-SPINE1 | Ethernet4/1 | 172.17.1.56/31 |
| DC1-POD1-LEAF2B | Ethernet30/1 | 172.17.1.59/31 | DC1-POD1-SPINE2 | Ethernet4/1 | 172.17.1.58/31 |
| DC1-POD1-LEAF2B | Ethernet31/1 | 172.17.1.61/31 | DC1-POD1-SPINE3 | Ethernet4/1 | 172.17.1.60/31 |
| DC1-POD1-LEAF2B | Ethernet32/1 | 172.17.1.63/31 | DC1-POD1-SPINE4 | Ethernet4/1 | 172.17.1.62/31 |
| DC1-POD1-LEAF3A | Ethernet29/1 | 172.17.1.65/31 | DC1-POD1-SPINE1 | Ethernet5/1 | 172.17.1.64/31 |
| DC1-POD1-LEAF3A | Ethernet30/1 | 172.17.1.67/31 | DC1-POD1-SPINE2 | Ethernet5/1 | 172.17.1.66/31 |
| DC1-POD1-LEAF3A | Ethernet31/1 | 172.17.1.69/31 | DC1-POD1-SPINE3 | Ethernet5/1 | 172.17.1.68/31 |
| DC1-POD1-LEAF3A | Ethernet32/1 | 172.17.1.71/31 | DC1-POD1-SPINE4 | Ethernet5/1 | 172.17.1.70/31 |
| DC1-POD1-LEAF3B | Ethernet29/1 | 172.17.1.73/31 | DC1-POD1-SPINE1 | Ethernet6/1 | 172.17.1.72/31 |
| DC1-POD1-LEAF3B | Ethernet30/1 | 172.17.1.75/31 | DC1-POD1-SPINE2 | Ethernet6/1 | 172.17.1.74/31 |
| DC1-POD1-LEAF3B | Ethernet31/1 | 172.17.1.77/31 | DC1-POD1-SPINE3 | Ethernet6/1 | 172.17.1.76/31 |
| DC1-POD1-LEAF3B | Ethernet32/1 | 172.17.1.79/31 | DC1-POD1-SPINE4 | Ethernet6/1 | 172.17.1.78/31 |
| DC1-POD1-LEAF4A | Ethernet29/1 | 172.17.1.81/31 | DC1-POD1-SPINE1 | Ethernet7/1 | 172.17.1.80/31 |
| DC1-POD1-LEAF4A | Ethernet30/1 | 172.17.1.83/31 | DC1-POD1-SPINE2 | Ethernet7/1 | 172.17.1.82/31 |
| DC1-POD1-LEAF4A | Ethernet31/1 | 172.17.1.85/31 | DC1-POD1-SPINE3 | Ethernet7/1 | 172.17.1.84/31 |
| DC1-POD1-LEAF4A | Ethernet32/1 | 172.17.1.87/31 | DC1-POD1-SPINE4 | Ethernet7/1 | 172.17.1.86/31 |
| DC1-POD1-LEAF4B | Ethernet29/1 | 172.17.1.89/31 | DC1-POD1-SPINE1 | Ethernet8/1 | 172.17.1.88/31 |
| DC1-POD1-LEAF4B | Ethernet30/1 | 172.17.1.91/31 | DC1-POD1-SPINE2 | Ethernet8/1 | 172.17.1.90/31 |
| DC1-POD1-LEAF4B | Ethernet31/1 | 172.17.1.93/31 | DC1-POD1-SPINE3 | Ethernet8/1 | 172.17.1.92/31 |
| DC1-POD1-LEAF4B | Ethernet32/1 | 172.17.1.95/31 | DC1-POD1-SPINE4 | Ethernet8/1 | 172.17.1.94/31 |
| DC1-POD1-LEAF5A | Ethernet29/1 | 172.17.1.97/31 | DC1-POD1-SPINE1 | Ethernet9/1 | 172.17.1.96/31 |
| DC1-POD1-LEAF5A | Ethernet30/1 | 172.17.1.99/31 | DC1-POD1-SPINE2 | Ethernet9/1 | 172.17.1.98/31 |
| DC1-POD1-LEAF5A | Ethernet31/1 | 172.17.1.101/31 | DC1-POD1-SPINE3 | Ethernet9/1 | 172.17.1.100/31 |
| DC1-POD1-LEAF5A | Ethernet32/1 | 172.17.1.103/31 | DC1-POD1-SPINE4 | Ethernet9/1 | 172.17.1.102/31 |
| DC1-POD1-LEAF5B | Ethernet29/1 | 172.17.1.105/31 | DC1-POD1-SPINE1 | Ethernet10/1 | 172.17.1.104/31 |
| DC1-POD1-LEAF5B | Ethernet30/1 | 172.17.1.107/31 | DC1-POD1-SPINE2 | Ethernet10/1 | 172.17.1.106/31 |
| DC1-POD1-LEAF5B | Ethernet31/1 | 172.17.1.109/31 | DC1-POD1-SPINE3 | Ethernet10/1 | 172.17.1.108/31 |
| DC1-POD1-LEAF5B | Ethernet32/1 | 172.17.1.111/31 | DC1-POD1-SPINE4 | Ethernet10/1 | 172.17.1.110/31 |
| DC1-POD1-LEAF6A | Ethernet29/1 | 172.17.1.113/31 | DC1-POD1-SPINE1 | Ethernet11/1 | 172.17.1.112/31 |
| DC1-POD1-LEAF6A | Ethernet30/1 | 172.17.1.115/31 | DC1-POD1-SPINE2 | Ethernet11/1 | 172.17.1.114/31 |
| DC1-POD1-LEAF6A | Ethernet31/1 | 172.17.1.117/31 | DC1-POD1-SPINE3 | Ethernet11/1 | 172.17.1.116/31 |
| DC1-POD1-LEAF6A | Ethernet32/1 | 172.17.1.119/31 | DC1-POD1-SPINE4 | Ethernet11/1 | 172.17.1.118/31 |
| DC1-POD1-LEAF6B | Ethernet29/1 | 172.17.1.121/31 | DC1-POD1-SPINE1 | Ethernet12/1 | 172.17.1.120/31 |
| DC1-POD1-LEAF6B | Ethernet30/1 | 172.17.1.123/31 | DC1-POD1-SPINE2 | Ethernet12/1 | 172.17.1.122/31 |
| DC1-POD1-LEAF6B | Ethernet31/1 | 172.17.1.125/31 | DC1-POD1-SPINE3 | Ethernet12/1 | 172.17.1.124/31 |
| DC1-POD1-LEAF6B | Ethernet32/1 | 172.17.1.127/31 | DC1-POD1-SPINE4 | Ethernet12/1 | 172.17.1.126/31 |
| DC1-POD1-LEAF7A | Ethernet29/1 | 172.17.1.129/31 | DC1-POD1-SPINE1 | Ethernet13/1 | 172.17.1.128/31 |
| DC1-POD1-LEAF7A | Ethernet30/1 | 172.17.1.131/31 | DC1-POD1-SPINE2 | Ethernet13/1 | 172.17.1.130/31 |
| DC1-POD1-LEAF7A | Ethernet31/1 | 172.17.1.133/31 | DC1-POD1-SPINE3 | Ethernet13/1 | 172.17.1.132/31 |
| DC1-POD1-LEAF7A | Ethernet32/1 | 172.17.1.135/31 | DC1-POD1-SPINE4 | Ethernet13/1 | 172.17.1.134/31 |
| DC1-POD1-LEAF7B | Ethernet29/1 | 172.17.1.137/31 | DC1-POD1-SPINE1 | Ethernet14/1 | 172.17.1.136/31 |
| DC1-POD1-LEAF7B | Ethernet30/1 | 172.17.1.139/31 | DC1-POD1-SPINE2 | Ethernet14/1 | 172.17.1.138/31 |
| DC1-POD1-LEAF7B | Ethernet31/1 | 172.17.1.141/31 | DC1-POD1-SPINE3 | Ethernet14/1 | 172.17.1.140/31 |
| DC1-POD1-LEAF7B | Ethernet32/1 | 172.17.1.143/31 | DC1-POD1-SPINE4 | Ethernet14/1 | 172.17.1.142/31 |
| DC1-POD1-LEAF8A | Ethernet29/1 | 172.17.1.145/31 | DC1-POD1-SPINE1 | Ethernet15/1 | 172.17.1.144/31 |
| DC1-POD1-LEAF8A | Ethernet30/1 | 172.17.1.147/31 | DC1-POD1-SPINE2 | Ethernet15/1 | 172.17.1.146/31 |
| DC1-POD1-LEAF8A | Ethernet31/1 | 172.17.1.149/31 | DC1-POD1-SPINE3 | Ethernet15/1 | 172.17.1.148/31 |
| DC1-POD1-LEAF8A | Ethernet32/1 | 172.17.1.151/31 | DC1-POD1-SPINE4 | Ethernet15/1 | 172.17.1.150/31 |
| DC1-POD1-LEAF8B | Ethernet29/1 | 172.17.1.153/31 | DC1-POD1-SPINE1 | Ethernet16/1 | 172.17.1.152/31 |
| DC1-POD1-LEAF8B | Ethernet30/1 | 172.17.1.155/31 | DC1-POD1-SPINE2 | Ethernet16/1 | 172.17.1.154/31 |
| DC1-POD1-LEAF8B | Ethernet31/1 | 172.17.1.157/31 | DC1-POD1-SPINE3 | Ethernet16/1 | 172.17.1.156/31 |
| DC1-POD1-LEAF8B | Ethernet32/1 | 172.17.1.159/31 | DC1-POD1-SPINE4 | Ethernet16/1 | 172.17.1.158/31 |
| DC1-POD1-LEAF9A | Ethernet29/1 | 172.17.1.161/31 | DC1-POD1-SPINE1 | Ethernet17/1 | 172.17.1.160/31 |
| DC1-POD1-LEAF9A | Ethernet30/1 | 172.17.1.163/31 | DC1-POD1-SPINE2 | Ethernet17/1 | 172.17.1.162/31 |
| DC1-POD1-LEAF9A | Ethernet31/1 | 172.17.1.165/31 | DC1-POD1-SPINE3 | Ethernet17/1 | 172.17.1.164/31 |
| DC1-POD1-LEAF9A | Ethernet32/1 | 172.17.1.167/31 | DC1-POD1-SPINE4 | Ethernet17/1 | 172.17.1.166/31 |
| DC1-POD1-LEAF9B | Ethernet29/1 | 172.17.1.169/31 | DC1-POD1-SPINE1 | Ethernet18/1 | 172.17.1.168/31 |
| DC1-POD1-LEAF9B | Ethernet30/1 | 172.17.1.171/31 | DC1-POD1-SPINE2 | Ethernet18/1 | 172.17.1.170/31 |
| DC1-POD1-LEAF9B | Ethernet31/1 | 172.17.1.173/31 | DC1-POD1-SPINE3 | Ethernet18/1 | 172.17.1.172/31 |
| DC1-POD1-LEAF9B | Ethernet32/1 | 172.17.1.175/31 | DC1-POD1-SPINE4 | Ethernet18/1 | 172.17.1.174/31 |
| DC1-POD1-LEAF10A | Ethernet29/1 | 172.17.1.177/31 | DC1-POD1-SPINE1 | Ethernet19/1 | 172.17.1.176/31 |
| DC1-POD1-LEAF10A | Ethernet30/1 | 172.17.1.179/31 | DC1-POD1-SPINE2 | Ethernet19/1 | 172.17.1.178/31 |
| DC1-POD1-LEAF10A | Ethernet31/1 | 172.17.1.181/31 | DC1-POD1-SPINE3 | Ethernet19/1 | 172.17.1.180/31 |
| DC1-POD1-LEAF10A | Ethernet32/1 | 172.17.1.183/31 | DC1-POD1-SPINE4 | Ethernet19/1 | 172.17.1.182/31 |
| DC1-POD1-LEAF10B | Ethernet29/1 | 172.17.1.185/31 | DC1-POD1-SPINE1 | Ethernet20/1 | 172.17.1.184/31 |
| DC1-POD1-LEAF10B | Ethernet30/1 | 172.17.1.187/31 | DC1-POD1-SPINE2 | Ethernet20/1 | 172.17.1.186/31 |
| DC1-POD1-LEAF10B | Ethernet31/1 | 172.17.1.189/31 | DC1-POD1-SPINE3 | Ethernet20/1 | 172.17.1.188/31 |
| DC1-POD1-LEAF10B | Ethernet32/1 | 172.17.1.191/31 | DC1-POD1-SPINE4 | Ethernet20/1 | 172.17.1.190/31 |
| DC1-POD1-LEAF11A | Ethernet29/1 | 172.17.1.193/31 | DC1-POD1-SPINE1 | Ethernet21/1 | 172.17.1.192/31 |
| DC1-POD1-LEAF11A | Ethernet30/1 | 172.17.1.195/31 | DC1-POD1-SPINE2 | Ethernet21/1 | 172.17.1.194/31 |
| DC1-POD1-LEAF11A | Ethernet31/1 | 172.17.1.197/31 | DC1-POD1-SPINE3 | Ethernet21/1 | 172.17.1.196/31 |
| DC1-POD1-LEAF11A | Ethernet32/1 | 172.17.1.199/31 | DC1-POD1-SPINE4 | Ethernet21/1 | 172.17.1.198/31 |
| DC1-POD1-LEAF11B | Ethernet29/1 | 172.17.1.201/31 | DC1-POD1-SPINE1 | Ethernet22/1 | 172.17.1.200/31 |
| DC1-POD1-LEAF11B | Ethernet30/1 | 172.17.1.203/31 | DC1-POD1-SPINE2 | Ethernet22/1 | 172.17.1.202/31 |
| DC1-POD1-LEAF11B | Ethernet31/1 | 172.17.1.205/31 | DC1-POD1-SPINE3 | Ethernet22/1 | 172.17.1.204/31 |
| DC1-POD1-LEAF11B | Ethernet32/1 | 172.17.1.207/31 | DC1-POD1-SPINE4 | Ethernet22/1 | 172.17.1.206/31 |
| DC1-POD1-LEAF12A | Ethernet29/1 | 172.17.1.209/31 | DC1-POD1-SPINE1 | Ethernet23/1 | 172.17.1.208/31 |
| DC1-POD1-LEAF12A | Ethernet30/1 | 172.17.1.211/31 | DC1-POD1-SPINE2 | Ethernet23/1 | 172.17.1.210/31 |
| DC1-POD1-LEAF12A | Ethernet31/1 | 172.17.1.213/31 | DC1-POD1-SPINE3 | Ethernet23/1 | 172.17.1.212/31 |
| DC1-POD1-LEAF12A | Ethernet32/1 | 172.17.1.215/31 | DC1-POD1-SPINE4 | Ethernet23/1 | 172.17.1.214/31 |
| DC1-POD1-LEAF12B | Ethernet29/1 | 172.17.1.217/31 | DC1-POD1-SPINE1 | Ethernet24/1 | 172.17.1.216/31 |
| DC1-POD1-LEAF12B | Ethernet30/1 | 172.17.1.219/31 | DC1-POD1-SPINE2 | Ethernet24/1 | 172.17.1.218/31 |
| DC1-POD1-LEAF12B | Ethernet31/1 | 172.17.1.221/31 | DC1-POD1-SPINE3 | Ethernet24/1 | 172.17.1.220/31 |
| DC1-POD1-LEAF12B | Ethernet32/1 | 172.17.1.223/31 | DC1-POD1-SPINE4 | Ethernet24/1 | 172.17.1.222/31 |
| DC1-POD1-LEAF13A | Ethernet29/1 | 172.17.1.225/31 | DC1-POD1-SPINE1 | Ethernet25/1 | 172.17.1.224/31 |
| DC1-POD1-LEAF13A | Ethernet30/1 | 172.17.1.227/31 | DC1-POD1-SPINE2 | Ethernet25/1 | 172.17.1.226/31 |
| DC1-POD1-LEAF13A | Ethernet31/1 | 172.17.1.229/31 | DC1-POD1-SPINE3 | Ethernet25/1 | 172.17.1.228/31 |
| DC1-POD1-LEAF13A | Ethernet32/1 | 172.17.1.231/31 | DC1-POD1-SPINE4 | Ethernet25/1 | 172.17.1.230/31 |
| DC1-POD1-LEAF13B | Ethernet29/1 | 172.17.1.233/31 | DC1-POD1-SPINE1 | Ethernet26/1 | 172.17.1.232/31 |
| DC1-POD1-LEAF13B | Ethernet30/1 | 172.17.1.235/31 | DC1-POD1-SPINE2 | Ethernet26/1 | 172.17.1.234/31 |
| DC1-POD1-LEAF13B | Ethernet31/1 | 172.17.1.237/31 | DC1-POD1-SPINE3 | Ethernet26/1 | 172.17.1.236/31 |
| DC1-POD1-LEAF13B | Ethernet32/1 | 172.17.1.239/31 | DC1-POD1-SPINE4 | Ethernet26/1 | 172.17.1.238/31 |
| DC1-POD1-LEAF14A | Ethernet29/1 | 172.17.1.241/31 | DC1-POD1-SPINE1 | Ethernet27/1 | 172.17.1.240/31 |
| DC1-POD1-LEAF14A | Ethernet30/1 | 172.17.1.243/31 | DC1-POD1-SPINE2 | Ethernet27/1 | 172.17.1.242/31 |
| DC1-POD1-LEAF14A | Ethernet31/1 | 172.17.1.245/31 | DC1-POD1-SPINE3 | Ethernet27/1 | 172.17.1.244/31 |
| DC1-POD1-LEAF14A | Ethernet32/1 | 172.17.1.247/31 | DC1-POD1-SPINE4 | Ethernet27/1 | 172.17.1.246/31 |
| DC1-POD1-LEAF14B | Ethernet29/1 | 172.17.1.249/31 | DC1-POD1-SPINE1 | Ethernet28/1 | 172.17.1.248/31 |
| DC1-POD1-LEAF14B | Ethernet30/1 | 172.17.1.251/31 | DC1-POD1-SPINE2 | Ethernet28/1 | 172.17.1.250/31 |
| DC1-POD1-LEAF14B | Ethernet31/1 | 172.17.1.253/31 | DC1-POD1-SPINE3 | Ethernet28/1 | 172.17.1.252/31 |
| DC1-POD1-LEAF14B | Ethernet32/1 | 172.17.1.255/31 | DC1-POD1-SPINE4 | Ethernet28/1 | 172.17.1.254/31 |
| DC1-POD1-SPINE1 | Ethernet29/1 | 172.16.1.1/31 | SUPER-SPINE1 | Ethernet1/1 | 172.16.1.0/31 |
| DC1-POD1-SPINE1 | Ethernet30/1 | 172.16.1.9/31 | SUPER-SPINE2 | Ethernet1/1 | 172.16.1.8/31 |
| DC1-POD1-SPINE1 | Ethernet31/1 | 172.16.1.17/31 | SUPER-SPINE3 | Ethernet1/1 | 172.16.1.16/31 |
| DC1-POD1-SPINE1 | Ethernet32/1 | 172.16.1.25/31 | SUPER-SPINE4 | Ethernet1/1 | 172.16.1.24/31 |
| DC1-POD1-SPINE2 | Ethernet29/1 | 172.16.1.3/31 | SUPER-SPINE1 | Ethernet2/1 | 172.16.1.2/31 |
| DC1-POD1-SPINE2 | Ethernet30/1 | 172.16.1.11/31 | SUPER-SPINE2 | Ethernet2/1 | 172.16.1.10/31 |
| DC1-POD1-SPINE2 | Ethernet31/1 | 172.16.1.19/31 | SUPER-SPINE3 | Ethernet2/1 | 172.16.1.18/31 |
| DC1-POD1-SPINE2 | Ethernet32/1 | 172.16.1.27/31 | SUPER-SPINE4 | Ethernet2/1 | 172.16.1.26/31 |
| DC1-POD1-SPINE3 | Ethernet29/1 | 172.16.1.5/31 | SUPER-SPINE1 | Ethernet3/1 | 172.16.1.4/31 |
| DC1-POD1-SPINE3 | Ethernet30/1 | 172.16.1.13/31 | SUPER-SPINE2 | Ethernet3/1 | 172.16.1.12/31 |
| DC1-POD1-SPINE3 | Ethernet31/1 | 172.16.1.21/31 | SUPER-SPINE3 | Ethernet3/1 | 172.16.1.20/31 |
| DC1-POD1-SPINE3 | Ethernet32/1 | 172.16.1.29/31 | SUPER-SPINE4 | Ethernet3/1 | 172.16.1.28/31 |
| DC1-POD1-SPINE4 | Ethernet29/1 | 172.16.1.7/31 | SUPER-SPINE1 | Ethernet4/1 | 172.16.1.6/31 |
| DC1-POD1-SPINE4 | Ethernet30/1 | 172.16.1.15/31 | SUPER-SPINE2 | Ethernet4/1 | 172.16.1.14/31 |
| DC1-POD1-SPINE4 | Ethernet31/1 | 172.16.1.23/31 | SUPER-SPINE3 | Ethernet4/1 | 172.16.1.22/31 |
| DC1-POD1-SPINE4 | Ethernet32/1 | 172.16.1.31/31 | SUPER-SPINE4 | Ethernet4/1 | 172.16.1.30/31 |
| DC1-POD2-LEAF1A | Ethernet29/1 | 172.17.2.1/31 | DC1-POD2-SPINE1 | Ethernet1/1 | 172.17.2.0/31 |
| DC1-POD2-LEAF1B | Ethernet29/1 | 172.17.2.9/31 | DC1-POD2-SPINE1 | Ethernet2/1 | 172.17.2.8/31 |
| DC1-POD2-LEAF2A | Ethernet29/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet3/1 | 172.17.2.16/31 |
| DC1-POD2-LEAF2B | Ethernet29/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet4/1 | 172.17.2.24/31 |
| DC1-POD2-LEAF3A | Ethernet29/1 | 172.17.2.33/31 | DC1-POD2-SPINE1 | Ethernet5/1 | 172.17.2.32/31 |
| DC1-POD2-LEAF3B | Ethernet29/1 | 172.17.2.41/31 | DC1-POD2-SPINE1 | Ethernet6/1 | 172.17.2.40/31 |
| DC1-POD2-LEAF4A | Ethernet29/1 | 172.17.2.49/31 | DC1-POD2-SPINE1 | Ethernet7/1 | 172.17.2.48/31 |
| DC1-POD2-LEAF4B | Ethernet29/1 | 172.17.2.57/31 | DC1-POD2-SPINE1 | Ethernet8/1 | 172.17.2.56/31 |
| DC1-POD2-LEAF5A | Ethernet29/1 | 172.17.2.65/31 | DC1-POD2-SPINE1 | Ethernet9/1 | 172.17.2.64/31 |
| DC1-POD2-LEAF5B | Ethernet29/1 | 172.17.2.73/31 | DC1-POD2-SPINE1 | Ethernet10/1 | 172.17.2.72/31 |
| DC1-POD2-LEAF6A | Ethernet29/1 | 172.17.2.81/31 | DC1-POD2-SPINE1 | Ethernet11/1 | 172.17.2.80/31 |
| DC1-POD2-LEAF6B | Ethernet29/1 | 172.17.2.89/31 | DC1-POD2-SPINE1 | Ethernet12/1 | 172.17.2.88/31 |
| DC1-POD2-LEAF7A | Ethernet29/1 | 172.17.2.97/31 | DC1-POD2-SPINE1 | Ethernet13/1 | 172.17.2.96/31 |
| DC1-POD2-LEAF7B | Ethernet29/1 | 172.17.2.105/31 | DC1-POD2-SPINE1 | Ethernet14/1 | 172.17.2.104/31 |
| DC1-POD2-LEAF8A | Ethernet29/1 | 172.17.2.113/31 | DC1-POD2-SPINE1 | Ethernet15/1 | 172.17.2.112/31 |
| DC1-POD2-LEAF8B | Ethernet29/1 | 172.17.2.121/31 | DC1-POD2-SPINE1 | Ethernet16/1 | 172.17.2.120/31 |
| DC1-POD2-LEAF9A | Ethernet29/1 | 172.17.2.129/31 | DC1-POD2-SPINE1 | Ethernet17/1 | 172.17.2.128/31 |
| DC1-POD2-LEAF9B | Ethernet29/1 | 172.17.2.137/31 | DC1-POD2-SPINE1 | Ethernet18/1 | 172.17.2.136/31 |
| DC1-POD2-LEAF10A | Ethernet29/1 | 172.17.2.145/31 | DC1-POD2-SPINE1 | Ethernet19/1 | 172.17.2.144/31 |
| DC1-POD2-LEAF10B | Ethernet29/1 | 172.17.2.153/31 | DC1-POD2-SPINE1 | Ethernet20/1 | 172.17.2.152/31 |
| DC1-POD2-LEAF11A | Ethernet29/1 | 172.17.2.161/31 | DC1-POD2-SPINE1 | Ethernet21/1 | 172.17.2.160/31 |
| DC1-POD2-LEAF11B | Ethernet29/1 | 172.17.2.169/31 | DC1-POD2-SPINE1 | Ethernet22/1 | 172.17.2.168/31 |
| DC1-POD2-LEAF12A | Ethernet29/1 | 172.17.2.177/31 | DC1-POD2-SPINE1 | Ethernet23/1 | 172.17.2.176/31 |
| DC1-POD2-LEAF12B | Ethernet29/1 | 172.17.2.185/31 | DC1-POD2-SPINE1 | Ethernet24/1 | 172.17.2.184/31 |
| DC1-POD2-LEAF13A | Ethernet29/1 | 172.17.2.193/31 | DC1-POD2-SPINE1 | Ethernet25/1 | 172.17.2.192/31 |
| DC1-POD2-LEAF13B | Ethernet29/1 | 172.17.2.201/31 | DC1-POD2-SPINE1 | Ethernet26/1 | 172.17.2.200/31 |
| DC1-POD2-LEAF14A | Ethernet29/1 | 172.17.2.209/31 | DC1-POD2-SPINE1 | Ethernet27/1 | 172.17.2.208/31 |
| DC1-POD2-LEAF14B | Ethernet29/1 | 172.17.2.217/31 | DC1-POD2-SPINE1 | Ethernet28/1 | 172.17.2.216/31 |
| DC1-POD2-SPINE1 | Ethernet29/1 | 172.16.2.1/31 | SUPER-SPINE1 | Ethernet5/1 | 172.16.2.0/31 |
| DC1-POD2-SPINE1 | Ethernet29/2 | 172.16.2.33/31 | SUPER-SPINE1 | Ethernet5/2 | 172.16.2.32/31 |
| DC1-POD2-SPINE1 | Ethernet29/3 | 172.16.2.65/31 | SUPER-SPINE2 | Ethernet5/3 | 172.16.2.64/31 |
| DC1-POD2-SPINE1 | Ethernet29/4 | 172.16.2.97/31 | SUPER-SPINE2 | Ethernet5/4 | 172.16.2.96/31 |
| DC1-POD2-SPINE1 | Ethernet30/1 | 172.16.2.129/31 | SUPER-SPINE3 | Ethernet6/1 | 172.16.2.128/31 |
| DC1-POD2-SPINE1 | Ethernet30/2 | 172.16.2.161/31 | SUPER-SPINE3 | Ethernet6/2 | 172.16.2.160/31 |
| DC1-POD2-SPINE1 | Ethernet30/3 | 172.16.2.193/31 | SUPER-SPINE4 | Ethernet6/3 | 172.16.2.192/31 |
| DC1-POD2-SPINE1 | Ethernet30/4 | 172.16.2.225/31 | SUPER-SPINE4 | Ethernet6/4 | 172.16.2.224/31 |
| DC2-POD1-LEAF1A | Ethernet28/1 | 200.200.200.102/24 | DC2-POD1-LEAF1B | Ethernet28/1 | 200.200.200.202/24 |
| DC2-POD1-LEAF1A | Ethernet29/1 | 172.17.32.1/31 | DC2-POD1-SPINE1 | Ethernet1/1 | 172.17.32.0/31 |
| DC2-POD1-LEAF1A | Ethernet30/1 | 172.17.32.3/31 | DC2-POD1-SPINE2 | Ethernet1/1 | 172.17.32.2/31 |
| DC2-POD1-LEAF1A | Ethernet31/1 | 172.17.32.5/31 | DC2-POD1-SPINE3 | Ethernet1/1 | 172.17.32.4/31 |
| DC2-POD1-LEAF1A | Ethernet32/1 | 172.17.32.7/31 | DC2-POD1-SPINE4 | Ethernet1/1 | 172.17.32.6/31 |
| DC2-POD1-LEAF1B | Ethernet29/1 | 172.17.32.9/31 | DC2-POD1-SPINE1 | Ethernet2/1 | 172.17.32.8/31 |
| DC2-POD1-LEAF1B | Ethernet30/1 | 172.17.32.11/31 | DC2-POD1-SPINE2 | Ethernet2/1 | 172.17.32.10/31 |
| DC2-POD1-LEAF1B | Ethernet31/1 | 172.17.32.13/31 | DC2-POD1-SPINE3 | Ethernet2/1 | 172.17.32.12/31 |
| DC2-POD1-LEAF1B | Ethernet32/1 | 172.17.32.15/31 | DC2-POD1-SPINE4 | Ethernet2/1 | 172.17.32.14/31 |
| DC2-POD1-LEAF2A | Ethernet29/1 | 172.17.32.17/31 | DC2-POD1-SPINE1 | Ethernet3/1 | 172.17.32.16/31 |
| DC2-POD1-LEAF2A | Ethernet30/1 | 172.17.32.19/31 | DC2-POD1-SPINE2 | Ethernet3/1 | 172.17.32.18/31 |
| DC2-POD1-LEAF2A | Ethernet31/1 | 172.17.32.21/31 | DC2-POD1-SPINE3 | Ethernet3/1 | 172.17.32.20/31 |
| DC2-POD1-LEAF2A | Ethernet32/1 | 172.17.32.23/31 | DC2-POD1-SPINE4 | Ethernet3/1 | 172.17.32.22/31 |
| DC2-POD1-LEAF2B | Ethernet29/1 | 172.17.32.25/31 | DC2-POD1-SPINE1 | Ethernet4/1 | 172.17.32.24/31 |
| DC2-POD1-LEAF2B | Ethernet30/1 | 172.17.32.27/31 | DC2-POD1-SPINE2 | Ethernet4/1 | 172.17.32.26/31 |
| DC2-POD1-LEAF2B | Ethernet31/1 | 172.17.32.29/31 | DC2-POD1-SPINE3 | Ethernet4/1 | 172.17.32.28/31 |
| DC2-POD1-LEAF2B | Ethernet32/1 | 172.17.32.31/31 | DC2-POD1-SPINE4 | Ethernet4/1 | 172.17.32.30/31 |
| DC2-POD1-LEAF3A | Ethernet29/1 | 172.17.32.33/31 | DC2-POD1-SPINE1 | Ethernet5/1 | 172.17.32.32/31 |
| DC2-POD1-LEAF3A | Ethernet30/1 | 172.17.32.35/31 | DC2-POD1-SPINE2 | Ethernet5/1 | 172.17.32.34/31 |
| DC2-POD1-LEAF3A | Ethernet31/1 | 172.17.32.37/31 | DC2-POD1-SPINE3 | Ethernet5/1 | 172.17.32.36/31 |
| DC2-POD1-LEAF3A | Ethernet32/1 | 172.17.32.39/31 | DC2-POD1-SPINE4 | Ethernet5/1 | 172.17.32.38/31 |
| DC2-POD1-LEAF3B | Ethernet29/1 | 172.17.32.41/31 | DC2-POD1-SPINE1 | Ethernet6/1 | 172.17.32.40/31 |
| DC2-POD1-LEAF3B | Ethernet30/1 | 172.17.32.43/31 | DC2-POD1-SPINE2 | Ethernet6/1 | 172.17.32.42/31 |
| DC2-POD1-LEAF3B | Ethernet31/1 | 172.17.32.45/31 | DC2-POD1-SPINE3 | Ethernet6/1 | 172.17.32.44/31 |
| DC2-POD1-LEAF3B | Ethernet32/1 | 172.17.32.47/31 | DC2-POD1-SPINE4 | Ethernet6/1 | 172.17.32.46/31 |
| DC2-POD1-LEAF4A | Ethernet29/1 | 172.17.32.49/31 | DC2-POD1-SPINE1 | Ethernet7/1 | 172.17.32.48/31 |
| DC2-POD1-LEAF4A | Ethernet30/1 | 172.17.32.51/31 | DC2-POD1-SPINE2 | Ethernet7/1 | 172.17.32.50/31 |
| DC2-POD1-LEAF4A | Ethernet31/1 | 172.17.32.53/31 | DC2-POD1-SPINE3 | Ethernet7/1 | 172.17.32.52/31 |
| DC2-POD1-LEAF4A | Ethernet32/1 | 172.17.32.55/31 | DC2-POD1-SPINE4 | Ethernet7/1 | 172.17.32.54/31 |
| DC2-POD1-LEAF4B | Ethernet29/1 | 172.17.32.57/31 | DC2-POD1-SPINE1 | Ethernet8/1 | 172.17.32.56/31 |
| DC2-POD1-LEAF4B | Ethernet30/1 | 172.17.32.59/31 | DC2-POD1-SPINE2 | Ethernet8/1 | 172.17.32.58/31 |
| DC2-POD1-LEAF4B | Ethernet31/1 | 172.17.32.61/31 | DC2-POD1-SPINE3 | Ethernet8/1 | 172.17.32.60/31 |
| DC2-POD1-LEAF4B | Ethernet32/1 | 172.17.32.63/31 | DC2-POD1-SPINE4 | Ethernet8/1 | 172.17.32.62/31 |
| DC2-POD1-LEAF5A | Ethernet29/1 | 172.17.32.65/31 | DC2-POD1-SPINE1 | Ethernet9/1 | 172.17.32.64/31 |
| DC2-POD1-LEAF5A | Ethernet30/1 | 172.17.32.67/31 | DC2-POD1-SPINE2 | Ethernet9/1 | 172.17.32.66/31 |
| DC2-POD1-LEAF5A | Ethernet31/1 | 172.17.32.69/31 | DC2-POD1-SPINE3 | Ethernet9/1 | 172.17.32.68/31 |
| DC2-POD1-LEAF5A | Ethernet32/1 | 172.17.32.71/31 | DC2-POD1-SPINE4 | Ethernet9/1 | 172.17.32.70/31 |
| DC2-POD1-LEAF5B | Ethernet29/1 | 172.17.32.73/31 | DC2-POD1-SPINE1 | Ethernet10/1 | 172.17.32.72/31 |
| DC2-POD1-LEAF5B | Ethernet30/1 | 172.17.32.75/31 | DC2-POD1-SPINE2 | Ethernet10/1 | 172.17.32.74/31 |
| DC2-POD1-LEAF5B | Ethernet31/1 | 172.17.32.77/31 | DC2-POD1-SPINE3 | Ethernet10/1 | 172.17.32.76/31 |
| DC2-POD1-LEAF5B | Ethernet32/1 | 172.17.32.79/31 | DC2-POD1-SPINE4 | Ethernet10/1 | 172.17.32.78/31 |
| DC2-POD1-LEAF6A | Ethernet29/1 | 172.17.32.81/31 | DC2-POD1-SPINE1 | Ethernet11/1 | 172.17.32.80/31 |
| DC2-POD1-LEAF6A | Ethernet30/1 | 172.17.32.83/31 | DC2-POD1-SPINE2 | Ethernet11/1 | 172.17.32.82/31 |
| DC2-POD1-LEAF6A | Ethernet31/1 | 172.17.32.85/31 | DC2-POD1-SPINE3 | Ethernet11/1 | 172.17.32.84/31 |
| DC2-POD1-LEAF6A | Ethernet32/1 | 172.17.32.87/31 | DC2-POD1-SPINE4 | Ethernet11/1 | 172.17.32.86/31 |
| DC2-POD1-LEAF6B | Ethernet29/1 | 172.17.32.89/31 | DC2-POD1-SPINE1 | Ethernet12/1 | 172.17.32.88/31 |
| DC2-POD1-LEAF6B | Ethernet30/1 | 172.17.32.91/31 | DC2-POD1-SPINE2 | Ethernet12/1 | 172.17.32.90/31 |
| DC2-POD1-LEAF6B | Ethernet31/1 | 172.17.32.93/31 | DC2-POD1-SPINE3 | Ethernet12/1 | 172.17.32.92/31 |
| DC2-POD1-LEAF6B | Ethernet32/1 | 172.17.32.95/31 | DC2-POD1-SPINE4 | Ethernet12/1 | 172.17.32.94/31 |
| DC2-POD1-LEAF7A | Ethernet29/1 | 172.17.32.97/31 | DC2-POD1-SPINE1 | Ethernet13/1 | 172.17.32.96/31 |
| DC2-POD1-LEAF7A | Ethernet30/1 | 172.17.32.99/31 | DC2-POD1-SPINE2 | Ethernet13/1 | 172.17.32.98/31 |
| DC2-POD1-LEAF7A | Ethernet31/1 | 172.17.32.101/31 | DC2-POD1-SPINE3 | Ethernet13/1 | 172.17.32.100/31 |
| DC2-POD1-LEAF7A | Ethernet32/1 | 172.17.32.103/31 | DC2-POD1-SPINE4 | Ethernet13/1 | 172.17.32.102/31 |
| DC2-POD1-LEAF7B | Ethernet29/1 | 172.17.32.105/31 | DC2-POD1-SPINE1 | Ethernet14/1 | 172.17.32.104/31 |
| DC2-POD1-LEAF7B | Ethernet30/1 | 172.17.32.107/31 | DC2-POD1-SPINE2 | Ethernet14/1 | 172.17.32.106/31 |
| DC2-POD1-LEAF7B | Ethernet31/1 | 172.17.32.109/31 | DC2-POD1-SPINE3 | Ethernet14/1 | 172.17.32.108/31 |
| DC2-POD1-LEAF7B | Ethernet32/1 | 172.17.32.111/31 | DC2-POD1-SPINE4 | Ethernet14/1 | 172.17.32.110/31 |
| DC2-POD1-LEAF8A | Ethernet29/1 | 172.17.32.113/31 | DC2-POD1-SPINE1 | Ethernet15/1 | 172.17.32.112/31 |
| DC2-POD1-LEAF8A | Ethernet30/1 | 172.17.32.115/31 | DC2-POD1-SPINE2 | Ethernet15/1 | 172.17.32.114/31 |
| DC2-POD1-LEAF8A | Ethernet31/1 | 172.17.32.117/31 | DC2-POD1-SPINE3 | Ethernet15/1 | 172.17.32.116/31 |
| DC2-POD1-LEAF8A | Ethernet32/1 | 172.17.32.119/31 | DC2-POD1-SPINE4 | Ethernet15/1 | 172.17.32.118/31 |
| DC2-POD1-LEAF8B | Ethernet29/1 | 172.17.32.121/31 | DC2-POD1-SPINE1 | Ethernet16/1 | 172.17.32.120/31 |
| DC2-POD1-LEAF8B | Ethernet30/1 | 172.17.32.123/31 | DC2-POD1-SPINE2 | Ethernet16/1 | 172.17.32.122/31 |
| DC2-POD1-LEAF8B | Ethernet31/1 | 172.17.32.125/31 | DC2-POD1-SPINE3 | Ethernet16/1 | 172.17.32.124/31 |
| DC2-POD1-LEAF8B | Ethernet32/1 | 172.17.32.127/31 | DC2-POD1-SPINE4 | Ethernet16/1 | 172.17.32.126/31 |
| DC2-POD1-LEAF9A | Ethernet29/1 | 172.17.32.129/31 | DC2-POD1-SPINE1 | Ethernet17/1 | 172.17.32.128/31 |
| DC2-POD1-LEAF9A | Ethernet30/1 | 172.17.32.131/31 | DC2-POD1-SPINE2 | Ethernet17/1 | 172.17.32.130/31 |
| DC2-POD1-LEAF9A | Ethernet31/1 | 172.17.32.133/31 | DC2-POD1-SPINE3 | Ethernet17/1 | 172.17.32.132/31 |
| DC2-POD1-LEAF9A | Ethernet32/1 | 172.17.32.135/31 | DC2-POD1-SPINE4 | Ethernet17/1 | 172.17.32.134/31 |
| DC2-POD1-LEAF9B | Ethernet29/1 | 172.17.32.137/31 | DC2-POD1-SPINE1 | Ethernet18/1 | 172.17.32.136/31 |
| DC2-POD1-LEAF9B | Ethernet30/1 | 172.17.32.139/31 | DC2-POD1-SPINE2 | Ethernet18/1 | 172.17.32.138/31 |
| DC2-POD1-LEAF9B | Ethernet31/1 | 172.17.32.141/31 | DC2-POD1-SPINE3 | Ethernet18/1 | 172.17.32.140/31 |
| DC2-POD1-LEAF9B | Ethernet32/1 | 172.17.32.143/31 | DC2-POD1-SPINE4 | Ethernet18/1 | 172.17.32.142/31 |
| DC2-POD1-LEAF10A | Ethernet29/1 | 172.17.32.145/31 | DC2-POD1-SPINE1 | Ethernet19/1 | 172.17.32.144/31 |
| DC2-POD1-LEAF10A | Ethernet30/1 | 172.17.32.147/31 | DC2-POD1-SPINE2 | Ethernet19/1 | 172.17.32.146/31 |
| DC2-POD1-LEAF10A | Ethernet31/1 | 172.17.32.149/31 | DC2-POD1-SPINE3 | Ethernet19/1 | 172.17.32.148/31 |
| DC2-POD1-LEAF10A | Ethernet32/1 | 172.17.32.151/31 | DC2-POD1-SPINE4 | Ethernet19/1 | 172.17.32.150/31 |
| DC2-POD1-LEAF10B | Ethernet29/1 | 172.17.32.153/31 | DC2-POD1-SPINE1 | Ethernet20/1 | 172.17.32.152/31 |
| DC2-POD1-LEAF10B | Ethernet30/1 | 172.17.32.155/31 | DC2-POD1-SPINE2 | Ethernet20/1 | 172.17.32.154/31 |
| DC2-POD1-LEAF10B | Ethernet31/1 | 172.17.32.157/31 | DC2-POD1-SPINE3 | Ethernet20/1 | 172.17.32.156/31 |
| DC2-POD1-LEAF10B | Ethernet32/1 | 172.17.32.159/31 | DC2-POD1-SPINE4 | Ethernet20/1 | 172.17.32.158/31 |
| DC2-POD1-LEAF11A | Ethernet29/1 | 172.17.32.161/31 | DC2-POD1-SPINE1 | Ethernet21/1 | 172.17.32.160/31 |
| DC2-POD1-LEAF11A | Ethernet30/1 | 172.17.32.163/31 | DC2-POD1-SPINE2 | Ethernet21/1 | 172.17.32.162/31 |
| DC2-POD1-LEAF11A | Ethernet31/1 | 172.17.32.165/31 | DC2-POD1-SPINE3 | Ethernet21/1 | 172.17.32.164/31 |
| DC2-POD1-LEAF11A | Ethernet32/1 | 172.17.32.167/31 | DC2-POD1-SPINE4 | Ethernet21/1 | 172.17.32.166/31 |
| DC2-POD1-LEAF11B | Ethernet29/1 | 172.17.32.169/31 | DC2-POD1-SPINE1 | Ethernet22/1 | 172.17.32.168/31 |
| DC2-POD1-LEAF11B | Ethernet30/1 | 172.17.32.171/31 | DC2-POD1-SPINE2 | Ethernet22/1 | 172.17.32.170/31 |
| DC2-POD1-LEAF11B | Ethernet31/1 | 172.17.32.173/31 | DC2-POD1-SPINE3 | Ethernet22/1 | 172.17.32.172/31 |
| DC2-POD1-LEAF11B | Ethernet32/1 | 172.17.32.175/31 | DC2-POD1-SPINE4 | Ethernet22/1 | 172.17.32.174/31 |
| DC2-POD1-LEAF12A | Ethernet29/1 | 172.17.32.177/31 | DC2-POD1-SPINE1 | Ethernet23/1 | 172.17.32.176/31 |
| DC2-POD1-LEAF12A | Ethernet30/1 | 172.17.32.179/31 | DC2-POD1-SPINE2 | Ethernet23/1 | 172.17.32.178/31 |
| DC2-POD1-LEAF12A | Ethernet31/1 | 172.17.32.181/31 | DC2-POD1-SPINE3 | Ethernet23/1 | 172.17.32.180/31 |
| DC2-POD1-LEAF12A | Ethernet32/1 | 172.17.32.183/31 | DC2-POD1-SPINE4 | Ethernet23/1 | 172.17.32.182/31 |
| DC2-POD1-LEAF12B | Ethernet29/1 | 172.17.32.185/31 | DC2-POD1-SPINE1 | Ethernet24/1 | 172.17.32.184/31 |
| DC2-POD1-LEAF12B | Ethernet30/1 | 172.17.32.187/31 | DC2-POD1-SPINE2 | Ethernet24/1 | 172.17.32.186/31 |
| DC2-POD1-LEAF12B | Ethernet31/1 | 172.17.32.189/31 | DC2-POD1-SPINE3 | Ethernet24/1 | 172.17.32.188/31 |
| DC2-POD1-LEAF12B | Ethernet32/1 | 172.17.32.191/31 | DC2-POD1-SPINE4 | Ethernet24/1 | 172.17.32.190/31 |
| DC2-POD1-LEAF13A | Ethernet29/1 | 172.17.32.193/31 | DC2-POD1-SPINE1 | Ethernet25/1 | 172.17.32.192/31 |
| DC2-POD1-LEAF13A | Ethernet30/1 | 172.17.32.195/31 | DC2-POD1-SPINE2 | Ethernet25/1 | 172.17.32.194/31 |
| DC2-POD1-LEAF13A | Ethernet31/1 | 172.17.32.197/31 | DC2-POD1-SPINE3 | Ethernet25/1 | 172.17.32.196/31 |
| DC2-POD1-LEAF13A | Ethernet32/1 | 172.17.32.199/31 | DC2-POD1-SPINE4 | Ethernet25/1 | 172.17.32.198/31 |
| DC2-POD1-LEAF13B | Ethernet29/1 | 172.17.32.201/31 | DC2-POD1-SPINE1 | Ethernet26/1 | 172.17.32.200/31 |
| DC2-POD1-LEAF13B | Ethernet30/1 | 172.17.32.203/31 | DC2-POD1-SPINE2 | Ethernet26/1 | 172.17.32.202/31 |
| DC2-POD1-LEAF13B | Ethernet31/1 | 172.17.32.205/31 | DC2-POD1-SPINE3 | Ethernet26/1 | 172.17.32.204/31 |
| DC2-POD1-LEAF13B | Ethernet32/1 | 172.17.32.207/31 | DC2-POD1-SPINE4 | Ethernet26/1 | 172.17.32.206/31 |
| DC2-POD1-LEAF14A | Ethernet29/1 | 172.17.32.209/31 | DC2-POD1-SPINE1 | Ethernet27/1 | 172.17.32.208/31 |
| DC2-POD1-LEAF14A | Ethernet30/1 | 172.17.32.211/31 | DC2-POD1-SPINE2 | Ethernet27/1 | 172.17.32.210/31 |
| DC2-POD1-LEAF14A | Ethernet31/1 | 172.17.32.213/31 | DC2-POD1-SPINE3 | Ethernet27/1 | 172.17.32.212/31 |
| DC2-POD1-LEAF14A | Ethernet32/1 | 172.17.32.215/31 | DC2-POD1-SPINE4 | Ethernet27/1 | 172.17.32.214/31 |
| DC2-POD1-LEAF14B | Ethernet29/1 | 172.17.32.217/31 | DC2-POD1-SPINE1 | Ethernet28/1 | 172.17.32.216/31 |
| DC2-POD1-LEAF14B | Ethernet30/1 | 172.17.32.219/31 | DC2-POD1-SPINE2 | Ethernet28/1 | 172.17.32.218/31 |
| DC2-POD1-LEAF14B | Ethernet31/1 | 172.17.32.221/31 | DC2-POD1-SPINE3 | Ethernet28/1 | 172.17.32.220/31 |
| DC2-POD1-LEAF14B | Ethernet32/1 | 172.17.32.223/31 | DC2-POD1-SPINE4 | Ethernet28/1 | 172.17.32.222/31 |
| DC2-POD1-SPINE1 | Ethernet29/1 | 172.16.32.1/31 | SUPER-SPINE1 | Ethernet9/1 | 172.16.32.0/31 |
| DC2-POD1-SPINE1 | Ethernet30/1 | 172.16.32.65/31 | SUPER-SPINE2 | Ethernet9/1 | 172.16.32.64/31 |
| DC2-POD1-SPINE1 | Ethernet31/1 | 172.16.32.129/31 | SUPER-SPINE3 | Ethernet9/1 | 172.16.32.128/31 |
| DC2-POD1-SPINE1 | Ethernet32/1 | 172.16.32.193/31 | SUPER-SPINE4 | Ethernet9/1 | 172.16.32.192/31 |
| DC2-POD1-SPINE2 | Ethernet29/1 | 172.16.32.3/31 | SUPER-SPINE1 | Ethernet10/1 | 172.16.32.2/31 |
| DC2-POD1-SPINE2 | Ethernet30/1 | 172.16.32.67/31 | SUPER-SPINE2 | Ethernet10/1 | 172.16.32.66/31 |
| DC2-POD1-SPINE2 | Ethernet31/1 | 172.16.32.131/31 | SUPER-SPINE3 | Ethernet10/1 | 172.16.32.130/31 |
| DC2-POD1-SPINE2 | Ethernet32/1 | 172.16.32.195/31 | SUPER-SPINE4 | Ethernet10/1 | 172.16.32.194/31 |
| DC2-POD1-SPINE3 | Ethernet29/1 | 172.16.32.5/31 | SUPER-SPINE1 | Ethernet11/1 | 172.16.32.4/31 |
| DC2-POD1-SPINE3 | Ethernet30/1 | 172.16.32.69/31 | SUPER-SPINE2 | Ethernet11/1 | 172.16.32.68/31 |
| DC2-POD1-SPINE3 | Ethernet31/1 | 172.16.32.133/31 | SUPER-SPINE3 | Ethernet11/1 | 172.16.32.132/31 |
| DC2-POD1-SPINE3 | Ethernet32/1 | 172.16.32.197/31 | SUPER-SPINE4 | Ethernet11/1 | 172.16.32.196/31 |
| DC2-POD1-SPINE4 | Ethernet29/1 | 172.16.32.7/31 | SUPER-SPINE1 | Ethernet12/1 | 172.16.32.6/31 |
| DC2-POD1-SPINE4 | Ethernet30/1 | 172.16.32.71/31 | SUPER-SPINE2 | Ethernet12/1 | 172.16.32.70/31 |
| DC2-POD1-SPINE4 | Ethernet31/1 | 172.16.32.135/31 | SUPER-SPINE3 | Ethernet12/1 | 172.16.32.134/31 |
| DC2-POD1-SPINE4 | Ethernet32/1 | 172.16.32.199/31 | SUPER-SPINE4 | Ethernet12/1 | 172.16.32.198/31 |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.4.1.0/24 | 256 | 28 | 10.94 % |
| 10.4.2.0/24 | 256 | 28 | 10.94 % |
| 10.4.27.0/24 | 256 | 5 | 1.96 % |
| 10.4.28.0/24 | 256 | 4 | 1.57 % |
| 10.4.29.0/24 | 256 | 1 | 0.4 % |
| 10.4.32.0/24 | 256 | 28 | 10.94 % |
| 10.4.58.0/24 | 256 | 4 | 1.57 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_POD1 | DC1-POD1-LEAF1A | 10.4.1.7/32 |
| DC1_POD1 | DC1-POD1-LEAF1B | 10.4.1.8/32 |
| DC1_POD1 | DC1-POD1-LEAF2A | 10.4.1.9/32 |
| DC1_POD1 | DC1-POD1-LEAF2B | 10.4.1.10/32 |
| DC1_POD1 | DC1-POD1-LEAF3A | 10.4.1.11/32 |
| DC1_POD1 | DC1-POD1-LEAF3B | 10.4.1.12/32 |
| DC1_POD1 | DC1-POD1-LEAF4A | 10.4.1.13/32 |
| DC1_POD1 | DC1-POD1-LEAF4B | 10.4.1.14/32 |
| DC1_POD1 | DC1-POD1-LEAF5A | 10.4.1.15/32 |
| DC1_POD1 | DC1-POD1-LEAF5B | 10.4.1.16/32 |
| DC1_POD1 | DC1-POD1-LEAF6A | 10.4.1.17/32 |
| DC1_POD1 | DC1-POD1-LEAF6B | 10.4.1.18/32 |
| DC1_POD1 | DC1-POD1-LEAF7A | 10.4.1.19/32 |
| DC1_POD1 | DC1-POD1-LEAF7B | 10.4.1.20/32 |
| DC1_POD1 | DC1-POD1-LEAF8A | 10.4.1.21/32 |
| DC1_POD1 | DC1-POD1-LEAF8B | 10.4.1.22/32 |
| DC1_POD1 | DC1-POD1-LEAF9A | 10.4.1.23/32 |
| DC1_POD1 | DC1-POD1-LEAF9B | 10.4.1.24/32 |
| DC1_POD1 | DC1-POD1-LEAF10A | 10.4.1.25/32 |
| DC1_POD1 | DC1-POD1-LEAF10B | 10.4.1.26/32 |
| DC1_POD1 | DC1-POD1-LEAF11A | 10.4.1.27/32 |
| DC1_POD1 | DC1-POD1-LEAF11B | 10.4.1.28/32 |
| DC1_POD1 | DC1-POD1-LEAF12A | 10.4.1.29/32 |
| DC1_POD1 | DC1-POD1-LEAF12B | 10.4.1.30/32 |
| DC1_POD1 | DC1-POD1-LEAF13A | 10.4.1.31/32 |
| DC1_POD1 | DC1-POD1-LEAF13B | 10.4.1.32/32 |
| DC1_POD1 | DC1-POD1-LEAF14A | 10.4.1.33/32 |
| DC1_POD1 | DC1-POD1-LEAF14B | 10.4.1.34/32 |
| DC1_POD1 | DC1-POD1-SPINE1 | 10.4.28.1/32 |
| DC1_POD1 | DC1-POD1-SPINE2 | 10.4.28.2/32 |
| DC1_POD1 | DC1-POD1-SPINE3 | 10.4.28.3/32 |
| DC1_POD1 | DC1-POD1-SPINE4 | 10.4.28.4/32 |
| DC1_POD2 | DC1-POD2-LEAF1A | 10.4.2.3/32 |
| DC1_POD2 | DC1-POD2-LEAF1B | 10.4.2.4/32 |
| DC1_POD2 | DC1-POD2-LEAF2A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF2B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF3A | 10.4.2.7/32 |
| DC1_POD2 | DC1-POD2-LEAF3B | 10.4.2.8/32 |
| DC1_POD2 | DC1-POD2-LEAF4A | 10.4.2.9/32 |
| DC1_POD2 | DC1-POD2-LEAF4B | 10.4.2.10/32 |
| DC1_POD2 | DC1-POD2-LEAF5A | 10.4.2.11/32 |
| DC1_POD2 | DC1-POD2-LEAF5B | 10.4.2.12/32 |
| DC1_POD2 | DC1-POD2-LEAF6A | 10.4.2.13/32 |
| DC1_POD2 | DC1-POD2-LEAF6B | 10.4.2.14/32 |
| DC1_POD2 | DC1-POD2-LEAF7A | 10.4.2.15/32 |
| DC1_POD2 | DC1-POD2-LEAF7B | 10.4.2.16/32 |
| DC1_POD2 | DC1-POD2-LEAF8A | 10.4.2.17/32 |
| DC1_POD2 | DC1-POD2-LEAF8B | 10.4.2.18/32 |
| DC1_POD2 | DC1-POD2-LEAF9A | 10.4.2.19/32 |
| DC1_POD2 | DC1-POD2-LEAF9B | 10.4.2.20/32 |
| DC1_POD2 | DC1-POD2-LEAF10A | 10.4.2.21/32 |
| DC1_POD2 | DC1-POD2-LEAF10B | 10.4.2.22/32 |
| DC1_POD2 | DC1-POD2-LEAF11A | 10.4.2.23/32 |
| DC1_POD2 | DC1-POD2-LEAF11B | 10.4.2.24/32 |
| DC1_POD2 | DC1-POD2-LEAF12A | 10.4.2.25/32 |
| DC1_POD2 | DC1-POD2-LEAF12B | 10.4.2.26/32 |
| DC1_POD2 | DC1-POD2-LEAF13A | 10.4.2.27/32 |
| DC1_POD2 | DC1-POD2-LEAF13B | 10.4.2.28/32 |
| DC1_POD2 | DC1-POD2-LEAF14A | 10.4.2.29/32 |
| DC1_POD2 | DC1-POD2-LEAF14B | 10.4.2.30/32 |
| DC1_POD2 | DC1-POD2-SPINE1 | 10.4.29.1/32 |
| DC2_POD1 | DC2-POD1-LEAF1A | 10.4.32.3/32 |
| DC2_POD1 | DC2-POD1-LEAF1B | 10.4.32.4/32 |
| DC2_POD1 | DC2-POD1-LEAF2A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF2B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF3A | 10.4.32.7/32 |
| DC2_POD1 | DC2-POD1-LEAF3B | 10.4.32.8/32 |
| DC2_POD1 | DC2-POD1-LEAF4A | 10.4.32.9/32 |
| DC2_POD1 | DC2-POD1-LEAF4B | 10.4.32.10/32 |
| DC2_POD1 | DC2-POD1-LEAF5A | 10.4.32.11/32 |
| DC2_POD1 | DC2-POD1-LEAF5B | 10.4.32.12/32 |
| DC2_POD1 | DC2-POD1-LEAF6A | 10.4.32.13/32 |
| DC2_POD1 | DC2-POD1-LEAF6B | 10.4.32.14/32 |
| DC2_POD1 | DC2-POD1-LEAF7A | 10.4.32.15/32 |
| DC2_POD1 | DC2-POD1-LEAF7B | 10.4.32.16/32 |
| DC2_POD1 | DC2-POD1-LEAF8A | 10.4.32.17/32 |
| DC2_POD1 | DC2-POD1-LEAF8B | 10.4.32.18/32 |
| DC2_POD1 | DC2-POD1-LEAF9A | 10.4.32.19/32 |
| DC2_POD1 | DC2-POD1-LEAF9B | 10.4.32.20/32 |
| DC2_POD1 | DC2-POD1-LEAF10A | 10.4.32.21/32 |
| DC2_POD1 | DC2-POD1-LEAF10B | 10.4.32.22/32 |
| DC2_POD1 | DC2-POD1-LEAF11A | 10.4.32.23/32 |
| DC2_POD1 | DC2-POD1-LEAF11B | 10.4.32.24/32 |
| DC2_POD1 | DC2-POD1-LEAF12A | 10.4.32.25/32 |
| DC2_POD1 | DC2-POD1-LEAF12B | 10.4.32.26/32 |
| DC2_POD1 | DC2-POD1-LEAF13A | 10.4.32.27/32 |
| DC2_POD1 | DC2-POD1-LEAF13B | 10.4.32.28/32 |
| DC2_POD1 | DC2-POD1-LEAF14A | 10.4.32.29/32 |
| DC2_POD1 | DC2-POD1-LEAF14B | 10.4.32.30/32 |
| DC2_POD1 | DC2-POD1-SPINE1 | 10.4.58.1/32 |
| DC2_POD1 | DC2-POD1-SPINE2 | 10.4.58.2/32 |
| DC2_POD1 | DC2-POD1-SPINE3 | 10.4.58.3/32 |
| DC2_POD1 | DC2-POD1-SPINE4 | 10.4.58.4/32 |
| AMS | SUPER-SPINE1 | 10.4.27.1/32 |
| AMS | SUPER-SPINE2 | 10.4.27.2/32 |
| AMS | SUPER-SPINE3 | 10.4.27.3/32 |
| AMS | SUPER-SPINE4 | 10.4.27.4/32 |
| AMS | SUPER-SPINE5 | 10.4.27.5/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 10.5.1.0/24 | 256 | 28 | 10.94 % |
| 10.5.2.0/24 | 256 | 28 | 10.94 % |
| 10.5.32.0/24 | 256 | 28 | 10.94 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC1_POD1 | DC1-POD1-LEAF1A | 10.5.1.7/32 |
| DC1_POD1 | DC1-POD1-LEAF1B | 10.5.1.7/32 |
| DC1_POD1 | DC1-POD1-LEAF2A | 10.5.1.9/32 |
| DC1_POD1 | DC1-POD1-LEAF2B | 10.5.1.9/32 |
| DC1_POD1 | DC1-POD1-LEAF3A | 10.5.1.11/32 |
| DC1_POD1 | DC1-POD1-LEAF3B | 10.5.1.11/32 |
| DC1_POD1 | DC1-POD1-LEAF4A | 10.5.1.13/32 |
| DC1_POD1 | DC1-POD1-LEAF4B | 10.5.1.13/32 |
| DC1_POD1 | DC1-POD1-LEAF5A | 10.5.1.15/32 |
| DC1_POD1 | DC1-POD1-LEAF5B | 10.5.1.15/32 |
| DC1_POD1 | DC1-POD1-LEAF6A | 10.5.1.17/32 |
| DC1_POD1 | DC1-POD1-LEAF6B | 10.5.1.17/32 |
| DC1_POD1 | DC1-POD1-LEAF7A | 10.5.1.19/32 |
| DC1_POD1 | DC1-POD1-LEAF7B | 10.5.1.19/32 |
| DC1_POD1 | DC1-POD1-LEAF8A | 10.5.1.21/32 |
| DC1_POD1 | DC1-POD1-LEAF8B | 10.5.1.21/32 |
| DC1_POD1 | DC1-POD1-LEAF9A | 10.5.1.23/32 |
| DC1_POD1 | DC1-POD1-LEAF9B | 10.5.1.23/32 |
| DC1_POD1 | DC1-POD1-LEAF10A | 10.5.1.25/32 |
| DC1_POD1 | DC1-POD1-LEAF10B | 10.5.1.25/32 |
| DC1_POD1 | DC1-POD1-LEAF11A | 10.5.1.27/32 |
| DC1_POD1 | DC1-POD1-LEAF11B | 10.5.1.27/32 |
| DC1_POD1 | DC1-POD1-LEAF12A | 10.5.1.29/32 |
| DC1_POD1 | DC1-POD1-LEAF12B | 10.5.1.29/32 |
| DC1_POD1 | DC1-POD1-LEAF13A | 10.5.1.31/32 |
| DC1_POD1 | DC1-POD1-LEAF13B | 10.5.1.31/32 |
| DC1_POD1 | DC1-POD1-LEAF14A | 10.5.1.33/32 |
| DC1_POD1 | DC1-POD1-LEAF14B | 10.5.1.33/32 |
| DC1_POD2 | DC1-POD2-LEAF1A | 10.5.2.3/32 |
| DC1_POD2 | DC1-POD2-LEAF1B | 10.5.2.3/32 |
| DC1_POD2 | DC1-POD2-LEAF2A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF2B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF3A | 10.5.2.7/32 |
| DC1_POD2 | DC1-POD2-LEAF3B | 10.5.2.7/32 |
| DC1_POD2 | DC1-POD2-LEAF4A | 10.5.2.9/32 |
| DC1_POD2 | DC1-POD2-LEAF4B | 10.5.2.9/32 |
| DC1_POD2 | DC1-POD2-LEAF5A | 10.5.2.11/32 |
| DC1_POD2 | DC1-POD2-LEAF5B | 10.5.2.11/32 |
| DC1_POD2 | DC1-POD2-LEAF6A | 10.5.2.13/32 |
| DC1_POD2 | DC1-POD2-LEAF6B | 10.5.2.13/32 |
| DC1_POD2 | DC1-POD2-LEAF7A | 10.5.2.15/32 |
| DC1_POD2 | DC1-POD2-LEAF7B | 10.5.2.15/32 |
| DC1_POD2 | DC1-POD2-LEAF8A | 10.5.2.17/32 |
| DC1_POD2 | DC1-POD2-LEAF8B | 10.5.2.17/32 |
| DC1_POD2 | DC1-POD2-LEAF9A | 10.5.2.19/32 |
| DC1_POD2 | DC1-POD2-LEAF9B | 10.5.2.19/32 |
| DC1_POD2 | DC1-POD2-LEAF10A | 10.5.2.21/32 |
| DC1_POD2 | DC1-POD2-LEAF10B | 10.5.2.21/32 |
| DC1_POD2 | DC1-POD2-LEAF11A | 10.5.2.23/32 |
| DC1_POD2 | DC1-POD2-LEAF11B | 10.5.2.23/32 |
| DC1_POD2 | DC1-POD2-LEAF12A | 10.5.2.25/32 |
| DC1_POD2 | DC1-POD2-LEAF12B | 10.5.2.25/32 |
| DC1_POD2 | DC1-POD2-LEAF13A | 10.5.2.27/32 |
| DC1_POD2 | DC1-POD2-LEAF13B | 10.5.2.27/32 |
| DC1_POD2 | DC1-POD2-LEAF14A | 10.5.2.29/32 |
| DC1_POD2 | DC1-POD2-LEAF14B | 10.5.2.29/32 |
| DC2_POD1 | DC2-POD1-LEAF1A | 10.5.32.3/32 |
| DC2_POD1 | DC2-POD1-LEAF1B | 10.5.32.3/32 |
| DC2_POD1 | DC2-POD1-LEAF2A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF2B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF3A | 10.5.32.7/32 |
| DC2_POD1 | DC2-POD1-LEAF3B | 10.5.32.7/32 |
| DC2_POD1 | DC2-POD1-LEAF4A | 10.5.32.9/32 |
| DC2_POD1 | DC2-POD1-LEAF4B | 10.5.32.9/32 |
| DC2_POD1 | DC2-POD1-LEAF5A | 10.5.32.11/32 |
| DC2_POD1 | DC2-POD1-LEAF5B | 10.5.32.11/32 |
| DC2_POD1 | DC2-POD1-LEAF6A | 10.5.32.13/32 |
| DC2_POD1 | DC2-POD1-LEAF6B | 10.5.32.13/32 |
| DC2_POD1 | DC2-POD1-LEAF7A | 10.5.32.15/32 |
| DC2_POD1 | DC2-POD1-LEAF7B | 10.5.32.15/32 |
| DC2_POD1 | DC2-POD1-LEAF8A | 10.5.32.17/32 |
| DC2_POD1 | DC2-POD1-LEAF8B | 10.5.32.17/32 |
| DC2_POD1 | DC2-POD1-LEAF9A | 10.5.32.19/32 |
| DC2_POD1 | DC2-POD1-LEAF9B | 10.5.32.19/32 |
| DC2_POD1 | DC2-POD1-LEAF10A | 10.5.32.21/32 |
| DC2_POD1 | DC2-POD1-LEAF10B | 10.5.32.21/32 |
| DC2_POD1 | DC2-POD1-LEAF11A | 10.5.32.23/32 |
| DC2_POD1 | DC2-POD1-LEAF11B | 10.5.32.23/32 |
| DC2_POD1 | DC2-POD1-LEAF12A | 10.5.32.25/32 |
| DC2_POD1 | DC2-POD1-LEAF12B | 10.5.32.25/32 |
| DC2_POD1 | DC2-POD1-LEAF13A | 10.5.32.27/32 |
| DC2_POD1 | DC2-POD1-LEAF13B | 10.5.32.27/32 |
| DC2_POD1 | DC2-POD1-LEAF14A | 10.5.32.29/32 |
| DC2_POD1 | DC2-POD1-LEAF14B | 10.5.32.29/32 |
