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
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1A | 192.168.1.7/24 Test without management IP | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1B | 192.168.1.8/24 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF2A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF2B | 192.168.1.9/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF3A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF3B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF4A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF4B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF5A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF5B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF6A | - | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF6B | 192.168.1.11/16 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF7A | - | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF7B | 192.168.1.11/16 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF8A | - | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF8B | 192.168.1.11/16 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF9A | - | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF9B | 192.168.1.11/16 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF10A | - | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF10B | 192.168.1.11/16 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF11A | - | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF11B | 192.168.1.11/16 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF12A | - | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF12B | 192.168.1.11/16 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF13A | - | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF13B | 192.168.1.11/16 | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF14A | - | 7280R | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF14B | 192.168.1.11/16 | 7280R | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE1 | - | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE2 | - | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE3 | - | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE4 | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF1A | 192.168.1.7/24 Test without management IP | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF1B | 192.168.1.8/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF2A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF2B | 192.168.1.9/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF3A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF3B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF4A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF4B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF5A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF5B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF6A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF6B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF7A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF7B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF8A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF8B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF9A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF9B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF10A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF10B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF11A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF11B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF12A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF12B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF13A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF13B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF14A | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF14B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE1 | 192.168.1.13/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE2 | 192.168.1.14/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE3 | 192.168.1.15/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE4 | 192.168.1.16/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF1A | 192.168.1.7/24 Test without management IP | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF1B | 192.168.1.8/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF2A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF2B | 192.168.1.9/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF3A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF3B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF4A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF4B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF5A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF5B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF6A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF6B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF7A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF7B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF8A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF8B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF9A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF9B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF10A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF10B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF11A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF11B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF12A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF12B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF13A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF13B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF14A | - | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF14B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE1 | 192.168.1.20/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE2 | 192.168.1.21/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE3 | 192.168.1.22/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE4 | 10.6.32.4/24 | vEOS-LAB | Provisioned |
| AMS | super-spine | SUPER-SPINE1 | 10.6.0.1/24 | 7280R | Provisioned |
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
| l3leaf | DC1-POD1-LEAF1A | Ethernet6 | l3leaf | DC1-POD1-LEAF1B | Ethernet4 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet15/1 | mlag_peer | DC1-POD1-LEAF1B | Ethernet15/1 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet16/1 | mlag_peer | DC1-POD1-LEAF1B | Ethernet16/1 |
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
| l3leaf | DC1-POD1-LEAF3A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet5/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet5/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet5/1 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet5/1 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet6/1 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet6/1 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet6/1 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet6/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet7/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet7/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet7/1 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet7/1 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet29/1 | spine | DC1-POD1-SPINE1 | Ethernet8/1 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet30/1 | spine | DC1-POD1-SPINE2 | Ethernet8/1 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet31/1 | spine | DC1-POD1-SPINE3 | Ethernet8/1 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet32/1 | spine | DC1-POD1-SPINE4 | Ethernet8/1 |
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
| spine | DC1-POD1-SPINE1 | Ethernet4 | l3leaf | DC2-POD1-LEAF14A | Ethernet29/1 |
| spine | DC1-POD1-SPINE1 | Ethernet5 | l3leaf | DC2-POD1-LEAF14B | Ethernet29/1 |
| spine | DC1-POD1-SPINE1 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet1/1 |
| spine | DC1-POD1-SPINE1 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet1/1 |
| spine | DC1-POD1-SPINE1 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet1/1 |
| spine | DC1-POD1-SPINE1 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet1/1 |
| spine | DC1-POD1-SPINE2 | Ethernet4 | l3leaf | DC2-POD1-LEAF14A | Ethernet30/1 |
| spine | DC1-POD1-SPINE2 | Ethernet5 | l3leaf | DC2-POD1-LEAF14B | Ethernet30/1 |
| spine | DC1-POD1-SPINE2 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet2/1 |
| spine | DC1-POD1-SPINE2 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet2/1 |
| spine | DC1-POD1-SPINE2 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet2/1 |
| spine | DC1-POD1-SPINE2 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet2/1 |
| spine | DC1-POD1-SPINE3 | Ethernet6 | l3leaf | DC2-POD1-LEAF2B | Ethernet31/1 |
| spine | DC1-POD1-SPINE3 | Ethernet7 | l3leaf | DC2-POD1-LEAF14A | Ethernet31/1 |
| spine | DC1-POD1-SPINE3 | Ethernet8 | l3leaf | DC2-POD1-LEAF14B | Ethernet31/1 |
| spine | DC1-POD1-SPINE3 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet3/1 |
| spine | DC1-POD1-SPINE3 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet3/1 |
| spine | DC1-POD1-SPINE3 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet3/1 |
| spine | DC1-POD1-SPINE3 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet3/1 |
| spine | DC1-POD1-SPINE4 | Ethernet7 | l3leaf | DC2-POD1-LEAF14A | Ethernet32/1 |
| spine | DC1-POD1-SPINE4 | Ethernet8 | l3leaf | DC2-POD1-LEAF14B | Ethernet32/1 |
| spine | DC1-POD1-SPINE4 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet4/1 |
| spine | DC1-POD1-SPINE4 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet4/1 |
| spine | DC1-POD1-SPINE4 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet4/1 |
| spine | DC1-POD1-SPINE4 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet4/1 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet5 | mlag_peer | DC1-POD2-LEAF1B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet6 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet6 | mlag_peer | DC1-POD2-LEAF1A | Ethernet6 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet6 |
| l3leaf | DC1-POD2-LEAF1B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet5 | mlag_peer | DC1-POD2-LEAF2B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet6 | mlag_peer | DC1-POD2-LEAF2B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet6 |
| l3leaf | DC1-POD2-LEAF2A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet6 |
| l3leaf | DC1-POD2-LEAF2B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet5 | mlag_peer | DC1-POD2-LEAF3B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet6 | mlag_peer | DC1-POD2-LEAF3B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF3A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF3B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet5 | mlag_peer | DC1-POD2-LEAF4B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet6 | mlag_peer | DC1-POD2-LEAF4B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF4A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF4B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet5 | mlag_peer | DC1-POD2-LEAF5B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet6 | mlag_peer | DC1-POD2-LEAF5B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF5A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF5B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet5 | mlag_peer | DC1-POD2-LEAF6B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet6 | mlag_peer | DC1-POD2-LEAF6B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF6A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF6B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet5 | mlag_peer | DC1-POD2-LEAF7B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet6 | mlag_peer | DC1-POD2-LEAF7B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF7A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF7B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet5 | mlag_peer | DC1-POD2-LEAF8B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet6 | mlag_peer | DC1-POD2-LEAF8B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF8A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF8B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet5 | mlag_peer | DC1-POD2-LEAF9B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet6 | mlag_peer | DC1-POD2-LEAF9B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF9A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF9B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet5 | mlag_peer | DC1-POD2-LEAF10B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet6 | mlag_peer | DC1-POD2-LEAF10B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF10A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF10B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet5 | mlag_peer | DC1-POD2-LEAF11B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet6 | mlag_peer | DC1-POD2-LEAF11B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF11A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF11B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet5 | mlag_peer | DC1-POD2-LEAF12B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet6 | mlag_peer | DC1-POD2-LEAF12B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF12A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF12B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet5 | mlag_peer | DC1-POD2-LEAF13B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet6 | mlag_peer | DC1-POD2-LEAF13B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF13A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF13B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet5 | mlag_peer | DC1-POD2-LEAF14B | Ethernet5 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet6 | mlag_peer | DC1-POD2-LEAF14B | Ethernet6 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF14A | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet29/1 | spine | DC1-POD2-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet30/1 | spine | DC1-POD2-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet31/1 | spine | DC1-POD2-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD2-LEAF14B | Ethernet32/1 | spine | DC1-POD2-SPINE4 | Ethernet8 |
| spine | DC1-POD2-SPINE1 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet5/1 |
| spine | DC1-POD2-SPINE1 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet5/1 |
| spine | DC1-POD2-SPINE1 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet5/1 |
| spine | DC1-POD2-SPINE1 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet5/1 |
| spine | DC1-POD2-SPINE2 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet6/1 |
| spine | DC1-POD2-SPINE2 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet6/1 |
| spine | DC1-POD2-SPINE2 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet6/1 |
| spine | DC1-POD2-SPINE2 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet6/1 |
| spine | DC1-POD2-SPINE3 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet7/1 |
| spine | DC1-POD2-SPINE3 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet7/1 |
| spine | DC1-POD2-SPINE3 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet7/1 |
| spine | DC1-POD2-SPINE3 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet7/1 |
| spine | DC1-POD2-SPINE4 | Ethernet29/1 | super-spine | SUPER-SPINE1 | Ethernet8/1 |
| spine | DC1-POD2-SPINE4 | Ethernet30/1 | super-spine | SUPER-SPINE2 | Ethernet8/1 |
| spine | DC1-POD2-SPINE4 | Ethernet31/1 | super-spine | SUPER-SPINE3 | Ethernet8/1 |
| spine | DC1-POD2-SPINE4 | Ethernet32/1 | super-spine | SUPER-SPINE4 | Ethernet8/1 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet5 | l3leaf | DC2-POD1-LEAF1B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet15/1 | mlag_peer | DC2-POD1-LEAF1B | Ethernet15/1 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet16/1 | mlag_peer | DC2-POD1-LEAF1B | Ethernet16/1 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet5 | mlag_peer | DC2-POD1-LEAF2B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet6 | mlag_peer | DC2-POD1-LEAF2B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet5 | mlag_peer | DC2-POD1-LEAF3B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF3A | Ethernet6 | mlag_peer | DC2-POD1-LEAF3B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet5 | mlag_peer | DC2-POD1-LEAF4B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF4A | Ethernet6 | mlag_peer | DC2-POD1-LEAF4B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet5 | mlag_peer | DC2-POD1-LEAF5B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF5A | Ethernet6 | mlag_peer | DC2-POD1-LEAF5B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet5 | mlag_peer | DC2-POD1-LEAF6B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF6A | Ethernet6 | mlag_peer | DC2-POD1-LEAF6B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet5 | mlag_peer | DC2-POD1-LEAF7B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF7A | Ethernet6 | mlag_peer | DC2-POD1-LEAF7B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet5 | mlag_peer | DC2-POD1-LEAF8B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF8A | Ethernet6 | mlag_peer | DC2-POD1-LEAF8B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet5 | mlag_peer | DC2-POD1-LEAF9B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF9A | Ethernet6 | mlag_peer | DC2-POD1-LEAF9B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet5 | mlag_peer | DC2-POD1-LEAF10B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF10A | Ethernet6 | mlag_peer | DC2-POD1-LEAF10B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet5 | mlag_peer | DC2-POD1-LEAF11B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF11A | Ethernet6 | mlag_peer | DC2-POD1-LEAF11B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet5 | mlag_peer | DC2-POD1-LEAF12B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF12A | Ethernet6 | mlag_peer | DC2-POD1-LEAF12B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet5 | mlag_peer | DC2-POD1-LEAF13B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF13A | Ethernet6 | mlag_peer | DC2-POD1-LEAF13B | Ethernet6 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet5 | mlag_peer | DC2-POD1-LEAF14B | Ethernet5 |
| l3leaf | DC2-POD1-LEAF14A | Ethernet6 | mlag_peer | DC2-POD1-LEAF14B | Ethernet6 |
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
| 172.16.2.0/24 | 256 | 32 | 12.5 % |
| 172.16.32.0/24 | 256 | 32 | 12.5 % |
| 172.17.1.0/24 | 256 | 224 | 87.5 % |
| 172.17.2.0/24 | 256 | 224 | 87.5 % |
| 172.17.32.0/24 | 256 | 18 | 7.04 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| DC1-POD1-LEAF1A | Ethernet6 | 11.1.0.0/31 | DC1-POD1-LEAF1B | Ethernet4 | 11.1.0.1/31 |
| DC1-POD1-LEAF1A | Ethernet29/1 | 172.17.1.1/31 | DC1-POD1-SPINE1 | Ethernet1/1 | 172.17.1.0/31 |
| DC1-POD1-LEAF1A | Ethernet30/1 | 172.17.1.3/31 | DC1-POD1-SPINE2 | Ethernet1/1 | 172.17.1.2/31 |
| DC1-POD1-LEAF1A | Ethernet31/1 | 172.17.1.5/31 | DC1-POD1-SPINE3 | Ethernet1/1 | 172.17.1.4/31 |
| DC1-POD1-LEAF1A | Ethernet32/1 | 172.17.1.7/31 | DC1-POD1-SPINE4 | Ethernet1/1 | 172.17.1.6/31 |
| DC1-POD1-LEAF1B | Ethernet29/1 | 172.17.1.9/31 | DC1-POD1-SPINE1 | Ethernet2/1 | 172.17.1.8/31 |
| DC1-POD1-LEAF1B | Ethernet30/1 | 172.17.1.11/31 | DC1-POD1-SPINE2 | Ethernet2/1 | 172.17.1.10/31 |
| DC1-POD1-LEAF1B | Ethernet31/1 | 172.17.1.13/31 | DC1-POD1-SPINE3 | Ethernet2/1 | 172.17.1.12/31 |
| DC1-POD1-LEAF1B | Ethernet32/1 | 172.17.1.15/31 | DC1-POD1-SPINE4 | Ethernet2/1 | 172.17.1.14/31 |
| DC1-POD1-LEAF2A | Ethernet29/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet3/1 | 172.17.1.16/31 |
| DC1-POD1-LEAF2A | Ethernet30/1 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet3/1 | 172.17.1.18/31 |
| DC1-POD1-LEAF2A | Ethernet31/1 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet3/1 | 172.17.1.20/31 |
| DC1-POD1-LEAF2A | Ethernet32/1 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet3/1 | 172.17.1.22/31 |
| DC1-POD1-LEAF2B | Ethernet29/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet4/1 | 172.17.1.24/31 |
| DC1-POD1-LEAF2B | Ethernet30/1 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet4/1 | 172.17.1.26/31 |
| DC1-POD1-LEAF2B | Ethernet31/1 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet4/1 | 172.17.1.28/31 |
| DC1-POD1-LEAF2B | Ethernet32/1 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet4/1 | 172.17.1.30/31 |
| DC1-POD1-LEAF3A | Ethernet29/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet5/1 | 172.17.1.16/31 |
| DC1-POD1-LEAF3A | Ethernet30/1 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet5/1 | 172.17.1.18/31 |
| DC1-POD1-LEAF3A | Ethernet31/1 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet5/1 | 172.17.1.20/31 |
| DC1-POD1-LEAF3A | Ethernet32/1 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet5/1 | 172.17.1.22/31 |
| DC1-POD1-LEAF3B | Ethernet29/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet6/1 | 172.17.1.24/31 |
| DC1-POD1-LEAF3B | Ethernet30/1 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet6/1 | 172.17.1.26/31 |
| DC1-POD1-LEAF3B | Ethernet31/1 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet6/1 | 172.17.1.28/31 |
| DC1-POD1-LEAF3B | Ethernet32/1 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet6/1 | 172.17.1.30/31 |
| DC1-POD1-LEAF4A | Ethernet29/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet7/1 | 172.17.1.16/31 |
| DC1-POD1-LEAF4A | Ethernet30/1 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet7/1 | 172.17.1.18/31 |
| DC1-POD1-LEAF4A | Ethernet31/1 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet7/1 | 172.17.1.20/31 |
| DC1-POD1-LEAF4A | Ethernet32/1 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet7/1 | 172.17.1.22/31 |
| DC1-POD1-LEAF4B | Ethernet29/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet8/1 | 172.17.1.24/31 |
| DC1-POD1-LEAF4B | Ethernet30/1 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet8/1 | 172.17.1.26/31 |
| DC1-POD1-LEAF4B | Ethernet31/1 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet8/1 | 172.17.1.28/31 |
| DC1-POD1-LEAF4B | Ethernet32/1 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet8/1 | 172.17.1.30/31 |
| DC1-POD1-LEAF5A | Ethernet29/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet9/1 | 172.17.1.16/31 |
| DC1-POD1-LEAF5A | Ethernet30/1 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet9/1 | 172.17.1.18/31 |
| DC1-POD1-LEAF5A | Ethernet31/1 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet9/1 | 172.17.1.20/31 |
| DC1-POD1-LEAF5A | Ethernet32/1 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet9/1 | 172.17.1.22/31 |
| DC1-POD1-LEAF5B | Ethernet29/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet10/1 | 172.17.1.24/31 |
| DC1-POD1-LEAF5B | Ethernet30/1 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet10/1 | 172.17.1.26/31 |
| DC1-POD1-LEAF5B | Ethernet31/1 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet10/1 | 172.17.1.28/31 |
| DC1-POD1-LEAF5B | Ethernet32/1 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet10/1 | 172.17.1.30/31 |
| DC1-POD1-LEAF6A | Ethernet29/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet11/1 | 172.17.1.16/31 |
| DC1-POD1-LEAF6A | Ethernet30/1 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet11/1 | 172.17.1.18/31 |
| DC1-POD1-LEAF6A | Ethernet31/1 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet11/1 | 172.17.1.20/31 |
| DC1-POD1-LEAF6A | Ethernet32/1 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet11/1 | 172.17.1.22/31 |
| DC1-POD1-LEAF6B | Ethernet29/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet12/1 | 172.17.1.24/31 |
| DC1-POD1-LEAF6B | Ethernet30/1 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet12/1 | 172.17.1.26/31 |
| DC1-POD1-LEAF6B | Ethernet31/1 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet12/1 | 172.17.1.28/31 |
| DC1-POD1-LEAF6B | Ethernet32/1 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet12/1 | 172.17.1.30/31 |
| DC1-POD1-LEAF7A | Ethernet29/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet13/1 | 172.17.1.16/31 |
| DC1-POD1-LEAF7A | Ethernet30/1 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet13/1 | 172.17.1.18/31 |
| DC1-POD1-LEAF7A | Ethernet31/1 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet13/1 | 172.17.1.20/31 |
| DC1-POD1-LEAF7A | Ethernet32/1 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet13/1 | 172.17.1.22/31 |
| DC1-POD1-LEAF7B | Ethernet29/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet14/1 | 172.17.1.24/31 |
| DC1-POD1-LEAF7B | Ethernet30/1 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet14/1 | 172.17.1.26/31 |
| DC1-POD1-LEAF7B | Ethernet31/1 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet14/1 | 172.17.1.28/31 |
| DC1-POD1-LEAF7B | Ethernet32/1 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet14/1 | 172.17.1.30/31 |
| DC1-POD1-LEAF8A | Ethernet29/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet15/1 | 172.17.1.16/31 |
| DC1-POD1-LEAF8A | Ethernet30/1 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet15/1 | 172.17.1.18/31 |
| DC1-POD1-LEAF8A | Ethernet31/1 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet15/1 | 172.17.1.20/31 |
| DC1-POD1-LEAF8A | Ethernet32/1 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet15/1 | 172.17.1.22/31 |
| DC1-POD1-LEAF8B | Ethernet29/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet16/1 | 172.17.1.24/31 |
| DC1-POD1-LEAF8B | Ethernet30/1 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet16/1 | 172.17.1.26/31 |
| DC1-POD1-LEAF8B | Ethernet31/1 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet16/1 | 172.17.1.28/31 |
| DC1-POD1-LEAF8B | Ethernet32/1 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet16/1 | 172.17.1.30/31 |
| DC1-POD1-LEAF9A | Ethernet29/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet17/1 | 172.17.1.16/31 |
| DC1-POD1-LEAF9A | Ethernet30/1 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet17/1 | 172.17.1.18/31 |
| DC1-POD1-LEAF9A | Ethernet31/1 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet17/1 | 172.17.1.20/31 |
| DC1-POD1-LEAF9A | Ethernet32/1 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet17/1 | 172.17.1.22/31 |
| DC1-POD1-LEAF9B | Ethernet29/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet18/1 | 172.17.1.24/31 |
| DC1-POD1-LEAF9B | Ethernet30/1 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet18/1 | 172.17.1.26/31 |
| DC1-POD1-LEAF9B | Ethernet31/1 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet18/1 | 172.17.1.28/31 |
| DC1-POD1-LEAF9B | Ethernet32/1 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet18/1 | 172.17.1.30/31 |
| DC1-POD1-LEAF10A | Ethernet29/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet19/1 | 172.17.1.16/31 |
| DC1-POD1-LEAF10A | Ethernet30/1 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet19/1 | 172.17.1.18/31 |
| DC1-POD1-LEAF10A | Ethernet31/1 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet19/1 | 172.17.1.20/31 |
| DC1-POD1-LEAF10A | Ethernet32/1 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet19/1 | 172.17.1.22/31 |
| DC1-POD1-LEAF10B | Ethernet29/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet20/1 | 172.17.1.24/31 |
| DC1-POD1-LEAF10B | Ethernet30/1 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet20/1 | 172.17.1.26/31 |
| DC1-POD1-LEAF10B | Ethernet31/1 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet20/1 | 172.17.1.28/31 |
| DC1-POD1-LEAF10B | Ethernet32/1 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet20/1 | 172.17.1.30/31 |
| DC1-POD1-LEAF11A | Ethernet29/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet21/1 | 172.17.1.16/31 |
| DC1-POD1-LEAF11A | Ethernet30/1 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet21/1 | 172.17.1.18/31 |
| DC1-POD1-LEAF11A | Ethernet31/1 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet21/1 | 172.17.1.20/31 |
| DC1-POD1-LEAF11A | Ethernet32/1 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet21/1 | 172.17.1.22/31 |
| DC1-POD1-LEAF11B | Ethernet29/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet22/1 | 172.17.1.24/31 |
| DC1-POD1-LEAF11B | Ethernet30/1 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet22/1 | 172.17.1.26/31 |
| DC1-POD1-LEAF11B | Ethernet31/1 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet22/1 | 172.17.1.28/31 |
| DC1-POD1-LEAF11B | Ethernet32/1 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet22/1 | 172.17.1.30/31 |
| DC1-POD1-LEAF12A | Ethernet29/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet23/1 | 172.17.1.16/31 |
| DC1-POD1-LEAF12A | Ethernet30/1 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet23/1 | 172.17.1.18/31 |
| DC1-POD1-LEAF12A | Ethernet31/1 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet23/1 | 172.17.1.20/31 |
| DC1-POD1-LEAF12A | Ethernet32/1 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet23/1 | 172.17.1.22/31 |
| DC1-POD1-LEAF12B | Ethernet29/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet24/1 | 172.17.1.24/31 |
| DC1-POD1-LEAF12B | Ethernet30/1 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet24/1 | 172.17.1.26/31 |
| DC1-POD1-LEAF12B | Ethernet31/1 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet24/1 | 172.17.1.28/31 |
| DC1-POD1-LEAF12B | Ethernet32/1 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet24/1 | 172.17.1.30/31 |
| DC1-POD1-LEAF13A | Ethernet29/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet25/1 | 172.17.1.16/31 |
| DC1-POD1-LEAF13A | Ethernet30/1 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet25/1 | 172.17.1.18/31 |
| DC1-POD1-LEAF13A | Ethernet31/1 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet25/1 | 172.17.1.20/31 |
| DC1-POD1-LEAF13A | Ethernet32/1 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet25/1 | 172.17.1.22/31 |
| DC1-POD1-LEAF13B | Ethernet29/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet26/1 | 172.17.1.24/31 |
| DC1-POD1-LEAF13B | Ethernet30/1 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet26/1 | 172.17.1.26/31 |
| DC1-POD1-LEAF13B | Ethernet31/1 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet26/1 | 172.17.1.28/31 |
| DC1-POD1-LEAF13B | Ethernet32/1 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet26/1 | 172.17.1.30/31 |
| DC1-POD1-LEAF14A | Ethernet29/1 | 172.17.1.17/31 | DC1-POD1-SPINE1 | Ethernet27/1 | 172.17.1.16/31 |
| DC1-POD1-LEAF14A | Ethernet30/1 | 172.17.1.19/31 | DC1-POD1-SPINE2 | Ethernet27/1 | 172.17.1.18/31 |
| DC1-POD1-LEAF14A | Ethernet31/1 | 172.17.1.21/31 | DC1-POD1-SPINE3 | Ethernet27/1 | 172.17.1.20/31 |
| DC1-POD1-LEAF14A | Ethernet32/1 | 172.17.1.23/31 | DC1-POD1-SPINE4 | Ethernet27/1 | 172.17.1.22/31 |
| DC1-POD1-LEAF14B | Ethernet29/1 | 172.17.1.25/31 | DC1-POD1-SPINE1 | Ethernet28/1 | 172.17.1.24/31 |
| DC1-POD1-LEAF14B | Ethernet30/1 | 172.17.1.27/31 | DC1-POD1-SPINE2 | Ethernet28/1 | 172.17.1.26/31 |
| DC1-POD1-LEAF14B | Ethernet31/1 | 172.17.1.29/31 | DC1-POD1-SPINE3 | Ethernet28/1 | 172.17.1.28/31 |
| DC1-POD1-LEAF14B | Ethernet32/1 | 172.17.1.31/31 | DC1-POD1-SPINE4 | Ethernet28/1 | 172.17.1.30/31 |
| DC1-POD1-SPINE1 | Ethernet4 | 172.17.32.16/31 | DC2-POD1-LEAF14A | Ethernet29/1 | 172.17.32.17/31 |
| DC1-POD1-SPINE1 | Ethernet5 | 172.17.32.24/31 | DC2-POD1-LEAF14B | Ethernet29/1 | 172.17.32.25/31 |
| DC1-POD1-SPINE1 | Ethernet29/1 | 172.16.1.1/31 | SUPER-SPINE1 | Ethernet1/1 | 172.16.1.0/31 |
| DC1-POD1-SPINE1 | Ethernet30/1 | 172.16.1.9/31 | SUPER-SPINE2 | Ethernet1/1 | 172.16.1.8/31 |
| DC1-POD1-SPINE1 | Ethernet31/1 | 172.16.1.17/31 | SUPER-SPINE3 | Ethernet1/1 | 172.16.1.16/31 |
| DC1-POD1-SPINE1 | Ethernet32/1 | 172.16.1.25/31 | SUPER-SPINE4 | Ethernet1/1 | 172.16.1.24/31 |
| DC1-POD1-SPINE2 | Ethernet4 | 172.17.32.18/31 | DC2-POD1-LEAF14A | Ethernet30/1 | 172.17.32.19/31 |
| DC1-POD1-SPINE2 | Ethernet5 | 172.17.32.26/31 | DC2-POD1-LEAF14B | Ethernet30/1 | 172.17.32.27/31 |
| DC1-POD1-SPINE2 | Ethernet29/1 | 172.16.1.3/31 | SUPER-SPINE1 | Ethernet2/1 | 172.16.1.2/31 |
| DC1-POD1-SPINE2 | Ethernet30/1 | 172.16.1.11/31 | SUPER-SPINE2 | Ethernet2/1 | 172.16.1.10/31 |
| DC1-POD1-SPINE2 | Ethernet31/1 | 172.16.1.19/31 | SUPER-SPINE3 | Ethernet2/1 | 172.16.1.18/31 |
| DC1-POD1-SPINE2 | Ethernet32/1 | 172.16.1.27/31 | SUPER-SPINE4 | Ethernet2/1 | 172.16.1.26/31 |
| DC1-POD1-SPINE3 | Ethernet6 | 172.17.32.28/31 | DC2-POD1-LEAF2B | Ethernet31/1 | 172.17.32.29/31 |
| DC1-POD1-SPINE3 | Ethernet7 | 172.17.32.20/31 | DC2-POD1-LEAF14A | Ethernet31/1 | 172.17.32.21/31 |
| DC1-POD1-SPINE3 | Ethernet8 | 172.17.32.28/31 | DC2-POD1-LEAF14B | Ethernet31/1 | 172.17.32.29/31 |
| DC1-POD1-SPINE3 | Ethernet29/1 | 172.16.1.5/31 | SUPER-SPINE1 | Ethernet3/1 | 172.16.1.4/31 |
| DC1-POD1-SPINE3 | Ethernet30/1 | 172.16.1.13/31 | SUPER-SPINE2 | Ethernet3/1 | 172.16.1.12/31 |
| DC1-POD1-SPINE3 | Ethernet31/1 | 172.16.1.21/31 | SUPER-SPINE3 | Ethernet3/1 | 172.16.1.20/31 |
| DC1-POD1-SPINE3 | Ethernet32/1 | 172.16.1.29/31 | SUPER-SPINE4 | Ethernet3/1 | 172.16.1.28/31 |
| DC1-POD1-SPINE4 | Ethernet7 | 172.17.32.22/31 | DC2-POD1-LEAF14A | Ethernet32/1 | 172.17.32.23/31 |
| DC1-POD1-SPINE4 | Ethernet8 | 172.17.32.30/31 | DC2-POD1-LEAF14B | Ethernet32/1 | 172.17.32.31/31 |
| DC1-POD1-SPINE4 | Ethernet29/1 | 172.16.1.7/31 | SUPER-SPINE1 | Ethernet4/1 | 172.16.1.6/31 |
| DC1-POD1-SPINE4 | Ethernet30/1 | 172.16.1.15/31 | SUPER-SPINE2 | Ethernet4/1 | 172.16.1.14/31 |
| DC1-POD1-SPINE4 | Ethernet31/1 | 172.16.1.23/31 | SUPER-SPINE3 | Ethernet4/1 | 172.16.1.22/31 |
| DC1-POD1-SPINE4 | Ethernet32/1 | 172.16.1.31/31 | SUPER-SPINE4 | Ethernet4/1 | 172.16.1.30/31 |
| DC1-POD2-LEAF1A | Ethernet29/1 | 172.17.2.1/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF1A | Ethernet30/1 | 172.17.2.3/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF1A | Ethernet31/1 | 172.17.2.5/31 | DC1-POD2-SPINE3 | Ethernet6 | 172.17.2.28/31 |
| DC1-POD2-LEAF1A | Ethernet32/1 | 172.17.2.7/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF1B | Ethernet29/1 | 172.17.2.9/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF1B | Ethernet30/1 | 172.17.2.11/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF1B | Ethernet31/1 | 172.17.2.13/31 | DC1-POD2-SPINE3 | Ethernet6 | 172.17.2.28/31 |
| DC1-POD2-LEAF1B | Ethernet32/1 | 172.17.2.15/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF2A | Ethernet29/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF2A | Ethernet30/1 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF2A | Ethernet31/1 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet6 | 172.17.2.28/31 |
| DC1-POD2-LEAF2A | Ethernet32/1 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF2B | Ethernet29/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF2B | Ethernet30/1 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF2B | Ethernet31/1 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet6 | 172.17.2.28/31 |
| DC1-POD2-LEAF2B | Ethernet32/1 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF3A | Ethernet29/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF3A | Ethernet30/1 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF3A | Ethernet31/1 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF3A | Ethernet32/1 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF3B | Ethernet29/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF3B | Ethernet30/1 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF3B | Ethernet31/1 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF3B | Ethernet32/1 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF4A | Ethernet29/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF4A | Ethernet30/1 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF4A | Ethernet31/1 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF4A | Ethernet32/1 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF4B | Ethernet29/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF4B | Ethernet30/1 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF4B | Ethernet31/1 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF4B | Ethernet32/1 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF5A | Ethernet29/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF5A | Ethernet30/1 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF5A | Ethernet31/1 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF5A | Ethernet32/1 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF5B | Ethernet29/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF5B | Ethernet30/1 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF5B | Ethernet31/1 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF5B | Ethernet32/1 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF6A | Ethernet29/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF6A | Ethernet30/1 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF6A | Ethernet31/1 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF6A | Ethernet32/1 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF6B | Ethernet29/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF6B | Ethernet30/1 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF6B | Ethernet31/1 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF6B | Ethernet32/1 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF7A | Ethernet29/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF7A | Ethernet30/1 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF7A | Ethernet31/1 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF7A | Ethernet32/1 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF7B | Ethernet29/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF7B | Ethernet30/1 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF7B | Ethernet31/1 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF7B | Ethernet32/1 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF8A | Ethernet29/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF8A | Ethernet30/1 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF8A | Ethernet31/1 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF8A | Ethernet32/1 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF8B | Ethernet29/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF8B | Ethernet30/1 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF8B | Ethernet31/1 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF8B | Ethernet32/1 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF9A | Ethernet29/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF9A | Ethernet30/1 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF9A | Ethernet31/1 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF9A | Ethernet32/1 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF9B | Ethernet29/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF9B | Ethernet30/1 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF9B | Ethernet31/1 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF9B | Ethernet32/1 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF10A | Ethernet29/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF10A | Ethernet30/1 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF10A | Ethernet31/1 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF10A | Ethernet32/1 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF10B | Ethernet29/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF10B | Ethernet30/1 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF10B | Ethernet31/1 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF10B | Ethernet32/1 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF11A | Ethernet29/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF11A | Ethernet30/1 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF11A | Ethernet31/1 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF11A | Ethernet32/1 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF11B | Ethernet29/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF11B | Ethernet30/1 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF11B | Ethernet31/1 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF11B | Ethernet32/1 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF12A | Ethernet29/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF12A | Ethernet30/1 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF12A | Ethernet31/1 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF12A | Ethernet32/1 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF12B | Ethernet29/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF12B | Ethernet30/1 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF12B | Ethernet31/1 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF12B | Ethernet32/1 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF13A | Ethernet29/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF13A | Ethernet30/1 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF13A | Ethernet31/1 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF13A | Ethernet32/1 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF13B | Ethernet29/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF13B | Ethernet30/1 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF13B | Ethernet31/1 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF13B | Ethernet32/1 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-LEAF14A | Ethernet29/1 | 172.17.2.17/31 | DC1-POD2-SPINE1 | Ethernet4 | 172.17.2.16/31 |
| DC1-POD2-LEAF14A | Ethernet30/1 | 172.17.2.19/31 | DC1-POD2-SPINE2 | Ethernet4 | 172.17.2.18/31 |
| DC1-POD2-LEAF14A | Ethernet31/1 | 172.17.2.21/31 | DC1-POD2-SPINE3 | Ethernet7 | 172.17.2.20/31 |
| DC1-POD2-LEAF14A | Ethernet32/1 | 172.17.2.23/31 | DC1-POD2-SPINE4 | Ethernet7 | 172.17.2.22/31 |
| DC1-POD2-LEAF14B | Ethernet29/1 | 172.17.2.25/31 | DC1-POD2-SPINE1 | Ethernet5 | 172.17.2.24/31 |
| DC1-POD2-LEAF14B | Ethernet30/1 | 172.17.2.27/31 | DC1-POD2-SPINE2 | Ethernet5 | 172.17.2.26/31 |
| DC1-POD2-LEAF14B | Ethernet31/1 | 172.17.2.29/31 | DC1-POD2-SPINE3 | Ethernet8 | 172.17.2.28/31 |
| DC1-POD2-LEAF14B | Ethernet32/1 | 172.17.2.31/31 | DC1-POD2-SPINE4 | Ethernet8 | 172.17.2.30/31 |
| DC1-POD2-SPINE1 | Ethernet29/1 | 172.16.2.1/31 | SUPER-SPINE1 | Ethernet5/1 | 172.16.2.0/31 |
| DC1-POD2-SPINE1 | Ethernet30/1 | 172.16.2.65/31 | SUPER-SPINE2 | Ethernet5/1 | 172.16.2.64/31 |
| DC1-POD2-SPINE1 | Ethernet31/1 | 172.16.2.129/31 | SUPER-SPINE3 | Ethernet5/1 | 172.16.2.128/31 |
| DC1-POD2-SPINE1 | Ethernet32/1 | 172.16.2.193/31 | SUPER-SPINE4 | Ethernet5/1 | 172.16.2.192/31 |
| DC1-POD2-SPINE2 | Ethernet29/1 | 172.16.2.3/31 | SUPER-SPINE1 | Ethernet6/1 | 172.16.2.2/31 |
| DC1-POD2-SPINE2 | Ethernet30/1 | 172.16.2.67/31 | SUPER-SPINE2 | Ethernet6/1 | 172.16.2.66/31 |
| DC1-POD2-SPINE2 | Ethernet31/1 | 172.16.2.131/31 | SUPER-SPINE3 | Ethernet6/1 | 172.16.2.130/31 |
| DC1-POD2-SPINE2 | Ethernet32/1 | 172.16.2.195/31 | SUPER-SPINE4 | Ethernet6/1 | 172.16.2.194/31 |
| DC1-POD2-SPINE3 | Ethernet29/1 | 172.16.2.5/31 | SUPER-SPINE1 | Ethernet7/1 | 172.16.2.4/31 |
| DC1-POD2-SPINE3 | Ethernet30/1 | 172.16.2.69/31 | SUPER-SPINE2 | Ethernet7/1 | 172.16.2.68/31 |
| DC1-POD2-SPINE3 | Ethernet31/1 | 172.16.2.133/31 | SUPER-SPINE3 | Ethernet7/1 | 172.16.2.132/31 |
| DC1-POD2-SPINE3 | Ethernet32/1 | 172.16.2.197/31 | SUPER-SPINE4 | Ethernet7/1 | 172.16.2.196/31 |
| DC1-POD2-SPINE4 | Ethernet29/1 | 172.16.2.7/31 | SUPER-SPINE1 | Ethernet8/1 | 172.16.2.6/31 |
| DC1-POD2-SPINE4 | Ethernet30/1 | 172.16.2.71/31 | SUPER-SPINE2 | Ethernet8/1 | 172.16.2.70/31 |
| DC1-POD2-SPINE4 | Ethernet31/1 | 172.16.2.135/31 | SUPER-SPINE3 | Ethernet8/1 | 172.16.2.134/31 |
| DC1-POD2-SPINE4 | Ethernet32/1 | 172.16.2.199/31 | SUPER-SPINE4 | Ethernet8/1 | 172.16.2.198/31 |
| DC2-POD1-LEAF1A | Ethernet5 | 11.1.1.18/31 | DC2-POD1-LEAF1B | Ethernet5 | 11.1.1.19/31 |
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
| 10.4.29.0/24 | 256 | 4 | 1.57 % |
| 10.4.32.0/24 | 256 | 28 | 10.94 % |
| 10.4.58.0/24 | 256 | 4 | 1.57 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_POD1 | DC1-POD1-LEAF1A | 10.4.1.3/32 |
| DC1_POD1 | DC1-POD1-LEAF1B | 10.4.1.4/32 |
| DC1_POD1 | DC1-POD1-LEAF2A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF2B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF3A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF3B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF4A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF4B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF5A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF5B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF6A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF6B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF7A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF7B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF8A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF8B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF9A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF9B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF10A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF10B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF11A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF11B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF12A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF12B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF13A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF13B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF14A | 10.4.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF14B | 10.4.1.6/32 |
| DC1_POD1 | DC1-POD1-SPINE1 | 10.4.28.1/32 |
| DC1_POD1 | DC1-POD1-SPINE2 | 10.4.28.2/32 |
| DC1_POD1 | DC1-POD1-SPINE3 | 10.4.28.3/32 |
| DC1_POD1 | DC1-POD1-SPINE4 | 10.4.28.4/32 |
| DC1_POD2 | DC1-POD2-LEAF1A | 10.4.2.3/32 |
| DC1_POD2 | DC1-POD2-LEAF1B | 10.4.2.4/32 |
| DC1_POD2 | DC1-POD2-LEAF2A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF2B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF3A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF3B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF4A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF4B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF5A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF5B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF6A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF6B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF7A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF7B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF8A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF8B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF9A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF9B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF10A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF10B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF11A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF11B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF12A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF12B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF13A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF13B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-LEAF14A | 10.4.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF14B | 10.4.2.6/32 |
| DC1_POD2 | DC1-POD2-SPINE1 | 10.4.29.1/32 |
| DC1_POD2 | DC1-POD2-SPINE2 | 10.4.29.2/32 |
| DC1_POD2 | DC1-POD2-SPINE3 | 10.4.29.3/32 |
| DC1_POD2 | DC1-POD2-SPINE4 | 10.4.29.4/32 |
| DC2_POD1 | DC2-POD1-LEAF1A | 10.4.32.3/32 |
| DC2_POD1 | DC2-POD1-LEAF1B | 10.4.32.4/32 |
| DC2_POD1 | DC2-POD1-LEAF2A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF2B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF3A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF3B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF4A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF4B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF5A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF5B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF6A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF6B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF7A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF7B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF8A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF8B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF9A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF9B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF10A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF10B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF11A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF11B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF12A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF12B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF13A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF13B | 10.4.32.6/32 |
| DC2_POD1 | DC2-POD1-LEAF14A | 10.4.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF14B | 10.4.32.6/32 |
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
| DC1_POD1 | DC1-POD1-LEAF1A | 10.5.1.3/32 |
| DC1_POD1 | DC1-POD1-LEAF1B | 10.5.1.3/32 |
| DC1_POD1 | DC1-POD1-LEAF2A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF2B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF3A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF3B | 10.5.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF4A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF4B | 10.5.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF5A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF5B | 10.5.1.6/32 |
| DC1_POD1 | DC1-POD1-LEAF6A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF6B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF7A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF7B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF8A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF8B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF9A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF9B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF10A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF10B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF11A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF11B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF12A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF12B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF13A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF13B | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF14A | 10.5.1.5/32 |
| DC1_POD1 | DC1-POD1-LEAF14B | 10.5.1.5/32 |
| DC1_POD2 | DC1-POD2-LEAF1A | 10.5.2.3/32 |
| DC1_POD2 | DC1-POD2-LEAF1B | 10.5.2.3/32 |
| DC1_POD2 | DC1-POD2-LEAF2A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF2B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF3A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF3B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF4A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF4B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF5A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF5B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF6A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF6B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF7A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF7B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF8A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF8B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF9A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF9B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF10A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF10B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF11A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF11B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF12A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF12B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF13A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF13B | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF14A | 10.5.2.5/32 |
| DC1_POD2 | DC1-POD2-LEAF14B | 10.5.2.5/32 |
| DC2_POD1 | DC2-POD1-LEAF1A | 10.5.32.3/32 |
| DC2_POD1 | DC2-POD1-LEAF1B | 10.5.32.3/32 |
| DC2_POD1 | DC2-POD1-LEAF2A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF2B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF3A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF3B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF4A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF4B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF5A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF5B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF6A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF6B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF7A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF7B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF8A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF8B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF9A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF9B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF10A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF10B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF11A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF11B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF12A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF12B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF13A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF13B | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF14A | 10.5.32.5/32 |
| DC2_POD1 | DC2-POD1-LEAF14B | 10.5.32.5/32 |
