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
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1B | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF2A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF2B | 192.168.1.9/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF3A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF3B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF4A | - | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF4B | 192.168.1.11/16 | vEOS-LAB | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF5A | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF5B | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF6A | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF6B | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF7A | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF7B | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF8A | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF8B | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF9A | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF9B | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF10A | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF10B | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF11A | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF11B | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF12A | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF12B | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF13A | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF13B | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF14A | - | - | Provisioned |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF14B | - | - | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE1 | - | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE2 | - | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE3 | - | vEOS-LAB | Provisioned |
| DC1_POD1 | spine | DC1-POD1-SPINE4 | - | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF1A | 192.168.1.17/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF1B | 192.168.1.18/24 | vEOS-LAB | Provisioned |
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
| DC1_POD2 | spine | DC1-POD2-SPINE1 | 192.168.1.13/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE2 | 192.168.1.14/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE3 | 192.168.1.15/24 | vEOS-LAB | Provisioned |
| DC1_POD2 | spine | DC1-POD2-SPINE4 | 192.168.1.16/24 | vEOS-LAB | Provisioned |
| DC1 | super-spine | DC1-SUPER-SPINE1 | 10.6.0.1/24 | vEOS-LAB | Provisioned |
| DC1 | super-spine | DC1-SUPER-SPINE2 | 10.6.0.2/24 | vEOS-LAB | Provisioned |
| DC1 | super-spine | DC1-SUPER-SPINE3 | 10.6.0.3/24 | vEOS-LAB | Provisioned |
| DC1 | super-spine | DC1-SUPER-SPINE4 | 10.6.0.4/24 | vEOS-LAB | Provisioned |
| DC1 | super-spine | DC1-SUPER-SPINE5 | 10.6.0.5/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF1A | 192.168.1.22/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE1 | 192.168.1.20/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE2 | 192.168.1.21/24 | vEOS-LAB | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE3 | - | - | Provisioned |
| DC2_POD1 | spine | DC2-POD1-SPINE4 | - | - | Provisioned |
| DC2 | super-spine | DC2-SUPER-SPINE1 | 10.6.64.1/24 | vEOS-LAB | Provisioned |
| DC2 | super-spine | DC2-SUPER-SPINE2 | 10.6.64.2/24 | vEOS-LAB | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | DC1-POD1-LEAF3A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet5 | mlag_peer | DC1-POD1-LEAF3B | Ethernet5 |
| l3leaf | DC1-POD1-LEAF3A | Ethernet6 | mlag_peer | DC1-POD1-LEAF3B | Ethernet6 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF3B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet4 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet7 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet5 | mlag_peer | DC1-POD1-LEAF4B | Ethernet5 |
| l3leaf | DC1-POD1-LEAF4A | Ethernet6 | mlag_peer | DC1-POD1-LEAF4B | Ethernet6 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet1/1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet1/2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet1/3 | spine | DC1-POD1-SPINE3 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF4B | Ethernet1/4 | spine | DC1-POD1-SPINE4 | Ethernet8 |
| spine | DC1-POD1-SPINE1 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet17/1 |
| spine | DC1-POD1-SPINE1 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet17/2 |
| spine | DC1-POD1-SPINE1 | Ethernet3 | super-spine | DC1-SUPER-SPINE3 | Ethernet17/3 |
| spine | DC1-POD1-SPINE2 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet17/1 |
| spine | DC1-POD1-SPINE2 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet17/2 |
| spine | DC1-POD1-SPINE2 | Ethernet3 | super-spine | DC1-SUPER-SPINE3 | Ethernet17/3 |
| spine | DC1-POD1-SPINE3 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet17/1 |
| spine | DC1-POD1-SPINE3 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet17/2 |
| spine | DC1-POD1-SPINE3 | Ethernet3 | super-spine | DC1-SUPER-SPINE3 | Ethernet17/3 |
| spine | DC1-POD1-SPINE3 | Ethernet4 | super-spine | DC1-SUPER-SPINE4 | Ethernet17/4 |
| spine | DC1-POD1-SPINE4 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet17/1 |
| spine | DC1-POD1-SPINE4 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet17/2 |
| spine | DC1-POD1-SPINE4 | Ethernet3 | super-spine | DC1-SUPER-SPINE3 | Ethernet17/3 |
| spine | DC1-POD1-SPINE4 | Ethernet4 | super-spine | DC1-SUPER-SPINE4 | Ethernet17/4 |
| spine | DC1-POD2-SPINE1 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet3 |
| spine | DC1-POD2-SPINE1 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet3 |
| spine | DC1-POD2-SPINE1 | Ethernet3 | l3leaf | DC1-POD2-LEAF1B | Ethernet1 |
| spine | DC1-POD2-SPINE2 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet4 |
| spine | DC1-POD2-SPINE2 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet4 |
| spine | DC1-POD2-SPINE2 | Ethernet3 | l3leaf | DC1-POD2-LEAF1B | Ethernet2 |
| spine | DC1-POD2-SPINE3 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet4 |
| spine | DC1-POD2-SPINE3 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet4 |
| spine | DC1-POD2-SPINE4 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet4 |
| spine | DC1-POD2-SPINE4 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet4 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet1 | spine | DC2-POD1-SPINE1 | Ethernet3 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet2 | spine | DC2-POD1-SPINE2 | Ethernet3 |
| spine | DC2-POD1-SPINE1 | Ethernet1 | super-spine | DC2-SUPER-SPINE1 | Ethernet1 |
| spine | DC2-POD1-SPINE1 | Ethernet2 | super-spine | DC2-SUPER-SPINE2 | Ethernet1 |
| spine | DC2-POD1-SPINE2 | Ethernet1 | super-spine | DC2-SUPER-SPINE1 | Ethernet2 |
| spine | DC2-POD1-SPINE2 | Ethernet2 | super-spine | DC2-SUPER-SPINE2 | Ethernet2 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.16.11.0/24 | 256 | 28 | 10.94 % |
| 172.16.12.0/24 | 256 | 16 | 6.25 % |
| 172.16.21.0/24 | 256 | 8 | 3.13 % |
| 172.17.110.0/24 | 256 | 32 | 12.5 % |
| 172.17.120.0/24 | 256 | 2 | 0.79 % |
| 172.17.210.0/24 | 256 | 4 | 1.57 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| DC1-POD1-LEAF3A | Ethernet1/1 | 172.17.110.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.110.16/31 |
| DC1-POD1-LEAF3A | Ethernet1/2 | 172.17.110.19/31 | DC1-POD1-SPINE2 | Ethernet4 | 172.17.110.18/31 |
| DC1-POD1-LEAF3A | Ethernet1/3 | 172.17.110.21/31 | DC1-POD1-SPINE3 | Ethernet7 | 172.17.110.20/31 |
| DC1-POD1-LEAF3A | Ethernet1/4 | 172.17.110.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.110.22/31 |
| DC1-POD1-LEAF3B | Ethernet1/1 | 172.17.110.25/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.110.24/31 |
| DC1-POD1-LEAF3B | Ethernet1/2 | 172.17.110.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.110.26/31 |
| DC1-POD1-LEAF3B | Ethernet1/3 | 172.17.110.29/31 | DC1-POD1-SPINE3 | Ethernet8 | 172.17.110.28/31 |
| DC1-POD1-LEAF3B | Ethernet1/4 | 172.17.110.31/31 | DC1-POD1-SPINE4 | Ethernet8 | 172.17.110.30/31 |
| DC1-POD1-LEAF4A | Ethernet1/1 | 172.17.110.17/31 | DC1-POD1-SPINE1 | Ethernet4 | 172.17.110.16/31 |
| DC1-POD1-LEAF4A | Ethernet1/2 | 172.17.110.19/31 | DC1-POD1-SPINE2 | Ethernet4 | 172.17.110.18/31 |
| DC1-POD1-LEAF4A | Ethernet1/3 | 172.17.110.21/31 | DC1-POD1-SPINE3 | Ethernet7 | 172.17.110.20/31 |
| DC1-POD1-LEAF4A | Ethernet1/4 | 172.17.110.23/31 | DC1-POD1-SPINE4 | Ethernet7 | 172.17.110.22/31 |
| DC1-POD1-LEAF4B | Ethernet1/1 | 172.17.110.25/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.110.24/31 |
| DC1-POD1-LEAF4B | Ethernet1/2 | 172.17.110.27/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.110.26/31 |
| DC1-POD1-LEAF4B | Ethernet1/3 | 172.17.110.29/31 | DC1-POD1-SPINE3 | Ethernet8 | 172.17.110.28/31 |
| DC1-POD1-LEAF4B | Ethernet1/4 | 172.17.110.31/31 | DC1-POD1-SPINE4 | Ethernet8 | 172.17.110.30/31 |
| DC1-POD1-SPINE1 | Ethernet1 | 172.16.11.1/31 | DC1-SUPER-SPINE1 | Ethernet17/1 | 172.16.11.6/31 |
| DC1-POD1-SPINE1 | Ethernet2 | 172.16.11.65/31 | DC1-SUPER-SPINE2 | Ethernet17/2 | 172.16.11.70/31 |
| DC1-POD1-SPINE1 | Ethernet3 | 172.16.11.129/31 | DC1-SUPER-SPINE3 | Ethernet17/3 | 172.16.11.134/31 |
| DC1-POD1-SPINE2 | Ethernet1 | 172.16.11.3/31 | DC1-SUPER-SPINE1 | Ethernet17/1 | 172.16.11.6/31 |
| DC1-POD1-SPINE2 | Ethernet2 | 172.16.11.67/31 | DC1-SUPER-SPINE2 | Ethernet17/2 | 172.16.11.70/31 |
| DC1-POD1-SPINE2 | Ethernet3 | 172.16.11.131/31 | DC1-SUPER-SPINE3 | Ethernet17/3 | 172.16.11.134/31 |
| DC1-POD1-SPINE3 | Ethernet1 | 172.16.11.5/31 | DC1-SUPER-SPINE1 | Ethernet17/1 | 172.16.11.6/31 |
| DC1-POD1-SPINE3 | Ethernet2 | 172.16.11.69/31 | DC1-SUPER-SPINE2 | Ethernet17/2 | 172.16.11.70/31 |
| DC1-POD1-SPINE3 | Ethernet3 | 172.16.11.133/31 | DC1-SUPER-SPINE3 | Ethernet17/3 | 172.16.11.134/31 |
| DC1-POD1-SPINE3 | Ethernet4 | 172.16.11.197/31 | DC1-SUPER-SPINE4 | Ethernet17/4 | 172.16.11.198/31 |
| DC1-POD1-SPINE4 | Ethernet1 | 172.16.11.7/31 | DC1-SUPER-SPINE1 | Ethernet17/1 | 172.16.11.6/31 |
| DC1-POD1-SPINE4 | Ethernet2 | 172.16.11.71/31 | DC1-SUPER-SPINE2 | Ethernet17/2 | 172.16.11.70/31 |
| DC1-POD1-SPINE4 | Ethernet3 | 172.16.11.135/31 | DC1-SUPER-SPINE3 | Ethernet17/3 | 172.16.11.134/31 |
| DC1-POD1-SPINE4 | Ethernet4 | 172.16.11.199/31 | DC1-SUPER-SPINE4 | Ethernet17/4 | 172.16.11.198/31 |
| DC1-POD2-SPINE1 | Ethernet1 | 172.16.12.1/31 | DC1-SUPER-SPINE1 | Ethernet3 | 172.16.12.0/31 |
| DC1-POD2-SPINE1 | Ethernet2 | 172.16.12.65/31 | DC1-SUPER-SPINE2 | Ethernet3 | 172.16.12.64/31 |
| DC1-POD2-SPINE2 | Ethernet1 | 172.16.12.3/31 | DC1-SUPER-SPINE1 | Ethernet4 | 172.16.12.6/31 |
| DC1-POD2-SPINE2 | Ethernet2 | 172.16.12.67/31 | DC1-SUPER-SPINE2 | Ethernet4 | 172.16.12.70/31 |
| DC1-POD2-SPINE3 | Ethernet1 | 172.16.12.5/31 | DC1-SUPER-SPINE1 | Ethernet4 | 172.16.12.6/31 |
| DC1-POD2-SPINE3 | Ethernet2 | 172.16.12.69/31 | DC1-SUPER-SPINE2 | Ethernet4 | 172.16.12.70/31 |
| DC1-POD2-SPINE4 | Ethernet1 | 172.16.12.7/31 | DC1-SUPER-SPINE1 | Ethernet4 | 172.16.12.6/31 |
| DC1-POD2-SPINE4 | Ethernet2 | 172.16.12.71/31 | DC1-SUPER-SPINE2 | Ethernet4 | 172.16.12.70/31 |
| DC2-POD1-LEAF1A | Ethernet1 | 172.17.210.1/31 | DC2-POD1-SPINE1 | Ethernet3 | 172.17.210.0/31 |
| DC2-POD1-LEAF1A | Ethernet2 | 172.17.210.3/31 | DC2-POD1-SPINE2 | Ethernet3 | 172.17.210.2/31 |
| DC2-POD1-SPINE1 | Ethernet1 | 172.16.21.1/31 | DC2-SUPER-SPINE1 | Ethernet1 | 172.16.21.0/31 |
| DC2-POD1-SPINE1 | Ethernet2 | 172.16.21.65/31 | DC2-SUPER-SPINE2 | Ethernet1 | 172.16.21.64/31 |
| DC2-POD1-SPINE2 | Ethernet1 | 172.16.21.3/31 | DC2-SUPER-SPINE1 | Ethernet2 | 172.16.21.2/31 |
| DC2-POD1-SPINE2 | Ethernet2 | 172.16.21.67/31 | DC2-SUPER-SPINE2 | Ethernet2 | 172.16.21.66/31 |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.4.0.0/24 | 256 | 5 | 1.96 % |
| 10.4.1.0/24 | 256 | 4 | 1.57 % |
| 10.4.2.0/24 | 256 | 4 | 1.57 % |
| 172.16.120.0/24 | 256 | 4 | 1.57 % |
| 172.16.200.0/24 | 256 | 2 | 0.79 % |
| 172.16.210.0/24 | 256 | 3 | 1.18 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_POD1 | DC1-POD1-LEAF3A | 10.4.2.5/32 |
| DC1_POD1 | DC1-POD1-LEAF3B | 10.4.2.6/32 |
| DC1_POD1 | DC1-POD1-LEAF4A | 10.4.2.5/32 |
| DC1_POD1 | DC1-POD1-LEAF4B | 10.4.2.6/32 |
| DC1_POD1 | DC1-POD1-SPINE1 | 10.4.1.1/32 |
| DC1_POD1 | DC1-POD1-SPINE2 | 10.4.1.2/32 |
| DC1_POD1 | DC1-POD1-SPINE3 | 10.4.1.3/32 |
| DC1_POD1 | DC1-POD1-SPINE4 | 10.4.1.4/32 |
| DC1_POD2 | DC1-POD2-SPINE1 | 172.16.120.1/32 |
| DC1_POD2 | DC1-POD2-SPINE2 | 172.16.120.2/32 |
| DC1_POD2 | DC1-POD2-SPINE3 | 172.16.120.3/32 |
| DC1_POD2 | DC1-POD2-SPINE4 | 172.16.120.4/32 |
| DC1 | DC1-SUPER-SPINE1 | 10.4.0.1/32 |
| DC1 | DC1-SUPER-SPINE2 | 10.4.0.2/32 |
| DC1 | DC1-SUPER-SPINE3 | 10.4.0.3/32 |
| DC1 | DC1-SUPER-SPINE4 | 10.4.0.4/32 |
| DC1 | DC1-SUPER-SPINE5 | 10.4.0.5/32 |
| DC2_POD1 | DC2-POD1-LEAF1A | 172.16.210.3/32 |
| DC2_POD1 | DC2-POD1-SPINE1 | 172.16.210.1/32 |
| DC2_POD1 | DC2-POD1-SPINE2 | 172.16.210.2/32 |
| DC2 | DC2-SUPER-SPINE1 | 172.16.200.1/32 |
| DC2 | DC2-SUPER-SPINE2 | 172.16.200.2/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 172.18.110.0/24 | 256 | 4 | 1.57 % |
| 172.18.120.0/24 | 256 | 0 | 0.0 % |
| 172.18.210.0/24 | 256 | 1 | 0.4 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC1_POD1 | DC1-POD1-LEAF3A | 172.18.110.5/32 |
| DC1_POD1 | DC1-POD1-LEAF3B | 172.18.110.5/32 |
| DC1_POD1 | DC1-POD1-LEAF4A | 172.18.110.5/32 |
| DC1_POD1 | DC1-POD1-LEAF4B | 172.18.110.5/32 |
| DC2_POD1 | DC2-POD1-LEAF1A | 172.18.210.3/32 |
