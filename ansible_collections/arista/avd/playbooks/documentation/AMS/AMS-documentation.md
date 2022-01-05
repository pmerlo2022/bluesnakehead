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
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1A | 10.6.1.20/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1B | 10.6.1.21/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF2A | 10.6.1.22/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF2B | 10.6.1.23/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF3A | 10.6.1.24/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF3B | 10.6.1.25/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF4A | 10.6.1.26/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF4B | 10.6.1.27/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF5A | 10.6.1.28/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF5B | 10.6.1.29/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF6A | 10.6.1.30/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF6B | 10.6.1.31/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF7A | 10.6.1.32/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF7B | 10.6.1.33/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF8A | 10.6.1.34/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF8B | 10.6.1.35/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF9A | 10.6.1.36/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF9B | 10.6.1.37/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF10A | 10.6.1.38/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF10B | 10.6.1.39/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF11A | 10.6.1.40/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF11B | 10.6.1.41/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF12A | 10.6.1.42/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF12B | 10.6.1.43/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF13A | 10.6.1.44/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF13B | 10.6.1.45/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF14A | 10.6.1.46/24 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF14B | 10.6.1.47/24 | 7280R | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE1 | 10.6.1.10/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE2 | 10.6.1.11/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE3 | 10.6.1.12/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE4 | 10.6.1.13/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF1A | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF1B | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF2A | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF2B | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF3A | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF3B | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF4A | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF4B | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF5A | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF5B | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF6A | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF6B | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF7A | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF7B | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF8A | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF8B | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF9A | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF9B | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF10A | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF10B | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF11A | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF11B | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF12A | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF12B | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF13A | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF13B | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF14A | - | - | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF14B | - | - | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE1 | - | - | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE2 | - | - | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE3 | - | - | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE4 | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF1A | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF1B | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF2A | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF2B | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF3A | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF3B | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF4A | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF4B | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF5A | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF5B | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF6A | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF6B | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF7A | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF7B | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF8A | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF8B | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF9A | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF9B | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF10A | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF10B | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF11A | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF11B | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF12A | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF12B | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF13A | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF13B | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF14A | - | - | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF14B | - | - | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE1 | - | - | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE2 | - | - | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE3 | - | - | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE4 | - | - | Provisioned |
| AMS | super-spine | SUPER-SPINE1 | - | - | Provisioned |
| AMS | super-spine | SUPER-SPINE2 | - | - | Provisioned |
| AMS | super-spine | SUPER-SPINE3 | - | - | Provisioned |
| AMS | super-spine | SUPER-SPINE4 | - | - | Provisioned |
| AMS | super-spine | SUPER-SPINE5 | - | - | Provisioned |

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

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.16.1.0/24 | 256 | 0 | 0.0 % |
| 172.17.1.0/24 | 256 | 224 | 87.5 % |

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

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.4.1.0/24 | 256 | 28 | 10.94 % |
| 10.4.28.0/24 | 256 | 4 | 1.57 % |

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

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 10.5.1.0/24 | 256 | 28 | 10.94 % |

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
